local bridge = require("bridge")
local commands = require("commands")
local addresses = require("addresses")
local field = require("field")
local missions = require("missions")
local chests = require("chests")
local scaling = require("scaling")
local endingReported = false
local previousGameState = 0
assert(memory and memory.set_u8, "This mod needs Yoki's Lua API 2 with memory access")
mod.on("frame", function()
    bridge.poll(function(packet)
        return commands.receive(packet, bridge)
    end)
    local gameState = memory.u32(addresses.GAMESTATE)
    if commands.gameReady(gameState) then
        if gameState ~= previousGameState then
            bridge.send(0x12, string.char(1))
        end
        field.character(commands, gameState)
        field.startup(gameState)
        field.gate(commands)
        field.result(bridge, gameState)
        scaling.poll(commands)
        missions.poll(commands)
        chests.poll(bridge)
        local ending = memory.u32(addresses.SCENEREC + addresses.SCENEID) == 8
        if ending and not endingReported then
            bridge.send(0x09, string.char(1))
        end
        endingReported = ending
    else
        gameState = 0
    end
    previousGameState = gameState
end)
