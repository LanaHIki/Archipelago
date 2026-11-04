import asyncio
from pathlib import Path
from uuid import uuid4
class NativeBridge:
    def __init__(self, directory):
        self.directory = Path(directory).expanduser().resolve()
        self.directory.mkdir(parents=True, exist_ok=True)
        self.session = uuid4().hex
        self.commands = {}
        self.command_sequence = 0
        self.command_acknowledged = 0
        self.last_inventory_query_sequence = 0
        self.event_acknowledged = 0
        self.received = bytearray()
        self.outgoing = bytearray()
        self.closed = False
        self.connected = False
        self.publish()
    def publish(self):
        lines = [self.session, str(self.event_acknowledged)]
        lines.extend(f"{sequence} {packet.hex()}" for sequence, packet in self.commands.items())
        temporary = self.directory / "client.writing"
        temporary.write_text("\n".join(lines) + "\n", encoding="ascii", newline="\n")
        try:
            temporary.replace(self.directory / "client.txt")
            self.publication_pending = False
        except PermissionError:
            self.publication_pending = True
    def write(self, packet):
        self.outgoing.extend(packet)
        while len(self.outgoing) >= 2 and len(self.outgoing) >= self.outgoing[1] + 2:
            size = self.outgoing[1] + 2
            self.command_sequence += 1
            if self.outgoing[0] == 0x10:
                self.last_inventory_query_sequence = self.command_sequence
            self.commands[self.command_sequence] = bytes(self.outgoing[:size])
            del self.outgoing[:size]
        self.publish()
    def poll(self):
        if self.publication_pending:
            self.publish()
        path = self.directory / "game.txt"
        if path.exists():
            lines = path.read_text(encoding="ascii").splitlines()
            if len(lines) >= 3 and lines[0] == self.session:
                acknowledged = int(lines[1])
                changed = not self.connected or acknowledged != self.command_acknowledged
                self.connected = True
                events = [(int(sequence), bytes.fromhex(packet))
                          for sequence, packet in (line.split(" ", 1) for line in lines[3:])]
                if self.command_acknowledged <= acknowledged <= self.command_sequence:
                    self.command_acknowledged = acknowledged
                    self.commands = {sequence: packet for sequence, packet in self.commands.items()
                                     if sequence > acknowledged}
                    for sequence, packet in events:
                        if sequence == self.event_acknowledged + 1:
                            self.received.extend(packet)
                            self.event_acknowledged = sequence
                            changed = True
                    if changed:
                        self.publish()
    async def drain(self):
        while self.publication_pending and not self.closed:
            self.publish()
            await asyncio.sleep(0.01)
        if self.closed:
            raise ConnectionResetError("Native Lua bridge closed")
    async def wait_for_acknowledgement(self):
        target = self.command_sequence
        while not self.closed and (not self.connected or self.command_acknowledged < target):
            self.poll()
            await asyncio.sleep(0.05)
        if self.closed:
            raise ConnectionResetError("Native Lua bridge closed")
    async def readexactly(self, size):
        while not self.closed and len(self.received) < size:
            self.poll()
            await asyncio.sleep(0.05)
        if len(self.received) < size:
            raise asyncio.IncompleteReadError(bytes(self.received), size)
        packet = bytes(self.received[:size])
        del self.received[:size]
        return packet
    def close(self):
        self.closed = True
