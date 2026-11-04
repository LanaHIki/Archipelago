import importlib.util
import asyncio
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import AsyncMock, patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("NativeBridge", ROOT / "client/NativeBridge.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class NativeBridgeTests(unittest.TestCase):
    def test_inventory_waits_for_its_own_connection_and_query(self):
        from worlds.khdays.client.commandHistory import DaysContext
        async def verify():
            with tempfile.TemporaryDirectory(dir=ROOT) as directory:
                context = DaysContext(None, None)
                bridge = MODULE.NativeBridge(directory)
                context.streams = bridge, bridge
                context.slot_data = {"connected": True}
                context.checkItemsAndSend = AsyncMock()
                with patch("worlds.khdays.client.commandHistory.NativeBridge", MODULE.NativeBridge):
                    syncing = asyncio.create_task(context.syncInventory())
                    await asyncio.sleep(.05)
                    query = bridge.last_inventory_query_sequence
                    for session, sequence in (("previous-connection", query), (bridge.session, query - 1)):
                        marker = sequence.to_bytes(4, "little") + session.encode("ascii")
                        await context.command_handeling(0x13, marker)
                        await context.command_handeling(0x11, bytes([0, 2, 0, 1]))
                        await context.command_handeling(0x11, bytes([3]))
                        await asyncio.sleep(.06)
                        self.assertFalse(syncing.done())
                        context.checkItemsAndSend.assert_not_awaited()
                    marker = query.to_bytes(4, "little") + bridge.session.encode("ascii")
                    await context.command_handeling(0x13, marker)
                    await context.command_handeling(0x11, bytes([0, 2, 0, 2]))
                    await context.command_handeling(0x11, bytes([3]))
                    await asyncio.wait_for(syncing, 1)
                    context.checkItemsAndSend.assert_awaited_once()
                    self.assertEqual(context.inventory[2], 2)
                await context.shutdown()
        asyncio.run(verify())

    def test_packets_acknowledgements_reload_and_reconnect(self):
        lua = shutil.which("lua") or r"C:\msys64\ucrt64\bin\lua.exe"
        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            mailbox = Path(directory)
            runner = mailbox / "run.lua"
            runner.write_text('''
local directory, script = ...
mod = {}
function mod.read(name)
    local file = io.open(directory .. "/" .. name, "rb")
    local content
    if file then
        content = file:read("*a")
        file:close()
    end
    return content
end
function mod.write(name, text)
    local file = assert(io.open(directory .. "/" .. name, "wb"))
    file:write(text)
    file:close()
    return true
end
local bridge = dofile(script)
bridge.poll(function(packet)
    bridge.send(0x11, packet)
    return true
end)
''', encoding="utf-8")
            def run_lua():
                subprocess.run([lua, str(runner), directory,
                                str(ROOT / "native_mod/scripts/bridge.lua")], check=True)
            bridge = MODULE.NativeBridge(directory)
            packet = bytes([1, 2, 0, 255])
            bridge.write(packet)
            run_lua()
            run_lua()
            bridge.poll()
            self.assertEqual(bridge.received, bytes([0x11, 4]) + packet)
            self.assertEqual(bridge.command_acknowledged, 1)
            self.assertEqual(bridge.commands, {})
            run_lua()
            bridge.write(bytes([0x10, 0]))
            run_lua()
            bridge.poll()
            self.assertEqual(bridge.event_acknowledged, 2)
            reconnect = MODULE.NativeBridge(directory)
            reconnect.write(bytes([3, 1, 14]))
            run_lua()
            reconnect.poll()
            self.assertEqual(reconnect.received, bytes([0x11, 2, 0x10, 0, 0x11, 3, 3, 1, 14]))
            async def exchange():
                with patch.object(Path, "replace", side_effect=PermissionError("Reader holds the mailbox")):
                    reconnect.publish()
                    self.assertTrue(reconnect.publication_pending)
                await reconnect.drain()
                self.assertFalse(reconnect.publication_pending)
                await reconnect.readexactly(len(reconnect.received))
                reconnect.write(bytes([6, 2, 1, 0]))
                await reconnect.drain()
                draining = asyncio.create_task(reconnect.wait_for_acknowledgement())
                await asyncio.to_thread(run_lua)
                await asyncio.wait_for(draining, 2)
                self.assertEqual(await reconnect.readexactly(1), bytes([0x11]))
                self.assertEqual(await reconnect.readexactly(1), bytes([4]))
                self.assertEqual(await reconnect.readexactly(4), bytes([6, 2, 1, 0]))
                reconnect.write(bytes([3]))
                reconnect.write(bytes([1, 14, 0x10, 0]))
                await asyncio.to_thread(run_lua)
                await asyncio.to_thread(run_lua)
                await asyncio.wait_for(reconnect.wait_for_acknowledgement(), 2)
                self.assertEqual(await reconnect.readexactly(9), bytes([0x11, 3, 3, 1, 14, 0x11, 2, 0x10, 0]))
                first = reconnect.command_sequence
                reconnect.write(bytes([0x10, 0]) * 40)
                await reconnect.drain()
                await asyncio.to_thread(run_lua)
                reconnect.poll()
                self.assertEqual(reconnect.command_acknowledged, first + 1)
                for _ in range(39):
                    await asyncio.to_thread(run_lua)
                    reconnect.poll()
                self.assertEqual(reconnect.command_acknowledged, first + 40)
                self.assertEqual(await reconnect.readexactly(160), bytes([0x11, 2, 0x10, 0]) * 40)
                waiting = asyncio.create_task(reconnect.readexactly(1))
                await asyncio.sleep(0)
                reconnect.close()
                with self.assertRaises(asyncio.IncompleteReadError):
                    await asyncio.wait_for(waiting, 2)
            asyncio.run(exchange())


if __name__ == "__main__":
    unittest.main()
