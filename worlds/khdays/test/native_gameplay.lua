local scripts = assert(...)
package.path = scripts .. "/?.lua;" .. package.path
local storedBytes = {}
local overlays = {}
local files = {}
local packets = {}
memory = {}
mod = {}
scene = {id = 2}
function mod.read(name)
    return files[name]
end
function mod.write(name, text)
    files[name] = text
    return true
end
function memory.loaded(overlay)
    return overlays[overlay] == true
end
for _, size in ipairs({1, 2, 4}) do
    memory["u" .. size * 8] = function(address)
        local value = 0
        for offset = 0, size - 1 do
            value = value | ((storedBytes[address + offset] or 0) << (offset * 8))
        end
        return value
    end
    memory["set_u" .. size * 8] = function(address, value)
        for offset = 0, size - 1 do
            storedBytes[address + offset] = (value >> (offset * 8)) & 255
        end
        return true
    end
end
local addresses = require("addresses")
local commands = require("commands")
local field = require("field")
local missions = require("missions")
local chests = require("chests")
local scaling = require("scaling")
local bridge = {commandSequence = 1, session = "fixture"}
function bridge.send(opcode, payload)
    packets[#packets + 1] = {opcode, payload}
end
local gameState = 0x20000000
memory.set_u32(addresses.GAMESTATE, gameState)
scene.id = 1
assert(not commands.receive(string.char(1, 2, 2, 0), bridge))
assert(memory.u8(gameState + addresses.ITEMCOUNT + 2) == 0)
scene.id = 8
assert(commands.gameReady(gameState))
scene.id = 2
assert(commands.receive(string.char(1, 2, 1, 0), bridge))
assert(memory.u8(gameState + addresses.ITEMCOUNT + 1) == 5)
assert(commands.receive(string.char(1, 2, 0x5D, 0), bridge))
assert(memory.u8(gameState + addresses.ITEMCOUNT + 0x5D) == 3)
assert(commands.receive(string.char(0x10, 0), bridge))
assert(#packets == 5 and packets[1][1] == 0x13 and #packets[2][2] == 253 and #packets[5][2] == 100)
assert(commands.receive(string.char(0x20, 2, 1, 14), bridge))
assert(commands.randomization == 1 and commands.missions[1].character == 14)
memory.set_u32(addresses.SCENEREC + addresses.SCENEID, 2)
memory.set_u32(addresses.SESSIONTAB, 1)
memory.set_u16(addresses.MISSIONID, 1)
memory.set_u8(gameState + addresses.XIONFLAGS, 255)
field.character(commands, gameState)
assert(memory.u32(addresses.SESSIONTAB + addresses.SESSIONKIND) == 14)
assert(memory.u8(addresses.MISSIONREC + addresses.MEMBERKIND) == 14)
assert(memory.u8(gameState + addresses.XIONFLAGS) == 247)
memory.set_u16(addresses.MISSIONID, 39)
field.character(commands, gameState)
assert(memory.u32(addresses.SESSIONTAB + addresses.SESSIONKIND) == 0)
overlays[2] = true
local context = 0x20010000
memory.set_u32(addresses.FIELDCONTEXT, context)
memory.set_u32(gameState + addresses.GAMEFLAGS, (7 << 23) | 123)
field.startup(gameState)
assert(memory.u32(gameState + addresses.GAMEFLAGS) == (357 << 23) | 123)
assert(memory.u32(addresses.SCENEREC + addresses.PENDINGID) == 2)
assert(memory.u16(addresses.DAYCLOCK + addresses.CLOCKMINUTES) == 0x2711)
memory.set_u16(addresses.MISSIONID, 1)
local beforeInitialResult = #packets
field.result(bridge, gameState)
assert(#packets == beforeInitialResult)
memory.set_u32(context + addresses.MISSIONTOTAL, 10)
memory.set_u32(context + addresses.MISSIONDONE, 10)
memory.set_u32(context + addresses.MISSIONGOAL, 8)
memory.set_u8(addresses.RESULTREC + addresses.RESULTFLAGS, 0x80)
field.result(bridge, gameState)
assert(memory.u8(addresses.RESULTREC + addresses.RESULTFLAGS) == 0x81)
assert(packets[#packets][1] == 7 and packets[#packets][2] == string.char(1, 2))
local packetCount = #packets
field.result(bridge, gameState)
assert(#packets == packetCount)
memory.set_u8(gameState + addresses.WITHDRAWFLAGS, 1)
memory.set_u8(addresses.RESULTREC + addresses.RESULTFLAGS, 0x81)
field.result(bridge, gameState)
assert(#packets == packetCount)
memory.set_u8(gameState + addresses.WITHDRAWFLAGS, 0)
memory.set_u8(addresses.RESULTREC + addresses.RESULTFLAGS, 0)
field.result(bridge, gameState)
assert(#packets == packetCount + 1)
local hud = 0x20018000
local option = 0x20019000
memory.set_u32(addresses.HUDCONTEXT, hud)
memory.set_u32(hud + addresses.HUDSECONDENTRY, option)
memory.set_u32(hud + addresses.HUDCURSOR, 0)
memory.set_u32(hud + addresses.HUDCOUNT, 2)
memory.set_u32(hud, 4)
for index = 1, 5 do
    memory.set_u16(option + (index - 1) * 2, string.byte("No...", index))
end
field.gate(commands)
assert(memory.u32(hud + addresses.HUDCURSOR) == 1)
commands.final = 1
memory.set_u32(hud + addresses.HUDCURSOR, 0)
field.gate(commands)
assert(memory.u32(hud + addresses.HUDCURSOR) == 0)
overlays[25] = true
local menuContext = 0x20040000
local page = 0x20050000
local manager = page + addresses.LISTMANAGER
local missionNode = 0x20060000
local dayPage = 0x20061000
local dayRows = 0x20062000
memory.set_u32(addresses.HOLOCONTEXT, menuContext)
memory.set_u32(menuContext + addresses.PAGEA, page)
memory.set_u32(manager + addresses.LISTHEAD, missionNode)
memory.set_u16(manager + addresses.LISTHEAD + addresses.LISTCOUNT, 1)
memory.set_u16(missionNode + addresses.NODEID, 1)
memory.set_u32(menuContext + addresses.PAGEB, dayPage)
memory.set_u32(addresses.PAGEBKIND, 5)
memory.set_u32(dayPage, 4)
memory.set_u32(dayPage + addresses.DAYROWS, dayRows)
memory.set_u32(dayPage + addresses.DAYCOUNT, 52)
memory.set_u32(dayPage + addresses.DAYSTRINGS, 0x20063000)
for index = 0, 55 do
    local day = index < 2 and 8 + index or 223 + index
    memory.set_u16(addresses.DAYTABLE + index * addresses.DAYTABLESTRIDE, day)
end
for _, settings in ipairs(commands.missions) do
    settings.hidden = 1
end
commands.missions[64].hidden = 0
missions.poll(commands)
assert(memory.u32(missionNode + addresses.NODEHIDDEN) == 1)
assert(memory.u32(dayPage + addresses.DAYCOUNT) == 1)
assert(memory.u32(dayRows) == 225)
assert(commands.receive(string.char(2, 2, 1, 0), bridge))
missions.poll(commands)
assert(memory.u32(missionNode + addresses.NODEHIDDEN) == 0)
assert(memory.u16(manager + addresses.LISTVISIBLE) == 1)
assert(memory.u32(dayPage + addresses.DAYCOUNT) == 2)
assert(memory.u32(dayRows) == 8)
assert(memory.u32(dayRows + addresses.DAYROWSTRIDE) == 225)
assert(memory.u32(dayPage + addresses.DAYSCROLLMAX) == 0)
assert(commands.receive(string.char(2, 2, 64, 1), bridge))
missions.poll(commands)
assert(memory.u32(dayPage + addresses.DAYCOUNT) == 1)
package.loaded.days = nil
require("days").poll(commands, menuContext)
assert(memory.u32(dayRows) == 8)
local objectTable = 0x20020000
local pool = 0x20021000
local chest = 0x20022000
memory.set_u32(addresses.OBJECTTABLE, objectTable)
memory.set_u32(objectTable + addresses.MODULES, pool)
memory.set_u16(pool + addresses.MODULEKIND, 11)
memory.set_u16(pool + addresses.MODULESTRIDE, 0x1BC)
memory.set_u16(pool + addresses.MODULECOUNT, 1)
memory.set_u32(pool + addresses.MODULEBASE, chest)
memory.set_u16(chest + addresses.OBJECTFLAGS, 8)
memory.set_u32(chest + addresses.OBJECTHANDLER, addresses.CHESTHANDLER)
memory.set_u8(chest + addresses.CHESTSTATE, 3)
memory.set_u16(chest + addresses.CHESTKEY, 0x123)
memory.set_u8(chest + addresses.CHESTSLOT, 2)
chests.poll(bridge)
assert(memory.u16(chest + addresses.CHESTKEY) == 0)
memory.set_u8(chest + addresses.CHESTSTATE, 5)
chests.poll(bridge)
assert(packets[#packets][1] == 8 and packets[#packets][2] == string.char(1, 2))
overlays[107] = true
local manager = 0x20030000
local node = 0x20031000
local slot = 0x20032000
local actor = 0x20033000
memory.set_u32(addresses.ENEMYMANAGER, manager)
memory.set_u32(manager + addresses.ENEMYLISTHEAD, node)
memory.set_u32(manager + addresses.ENEMYLISTCOUNT, 1)
memory.set_u32(node + addresses.ENEMYNEXT, manager + addresses.ENEMYLISTEND)
memory.set_u32(node + addresses.ENEMYSLOT, slot)
memory.set_u32(slot, actor)
memory.set_u16(actor, 0x60)
memory.set_u16(addresses.MISSIONID, 91)
memory.set_u16(actor + addresses.ENEMYMAXHP, 100)
for index = 0, 7 do
    memory.set_u16(actor + addresses.ENEMYOFFENSE + index * 6, 100)
    memory.set_u16(actor + addresses.ENEMYDEFENSE + index * 2, 100)
end
scaling.poll(commands)
assert(memory.u16(actor + addresses.ENEMYMAXHP) == 60)
assert(memory.u16(actor + addresses.ENEMYHP) == 60)
assert(memory.u16(actor + addresses.ENEMYOFFENSE) == 10)
assert(memory.u16(actor + addresses.ENEMYDEFENSE) == 10)
commands.missions[1].hidden = 1
package.loaded.commands = nil
local restored = require("commands")
assert(restored.missions[1].hidden == 0)
assert(restored.missions[1].character == 14 and restored.randomization == 1)
local frameCallback
function mod.on(event, callback)
    assert(event == "frame")
    frameCallback = callback
end
for overlay in pairs(overlays) do
    overlays[overlay] = false
end
scene.id = 8
memory.set_u32(addresses.SCENEREC + addresses.SCENEID, 8)
files["client.txt"] = "pipeline\n0\n1 1000\n"
require("main")
frameCallback()
frameCallback()
frameCallback()
local endingPackets = 0
for packet in files["game.txt"]:gmatch("\n%d+ (%x+)") do
    if packet == "090101" then
        endingPackets = endingPackets + 1
    end
end
assert(endingPackets == 1)
print("Native Lua gameplay fixtures passed")
