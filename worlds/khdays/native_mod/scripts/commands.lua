local addresses = require("addresses")
local database = require("database")
local commands = {character = 0, completed = 0, final = 0, randomization = 0}
commands.missions = database.missions
function commands.gameReady(gameState)
    return gameState ~= 0 and (scene.id == 2 or scene.id == 5 or scene.id == 6 or scene.id == 8 or scene.id == 19)
end
local function saveSettings()
    local lines = {commands.character, commands.completed, commands.final, commands.randomization}
    for mission = 1, 91 do
        local settings = commands.missions[mission]
        lines[#lines + 1] = settings.hidden .. " " .. settings.character
    end
    assert(mod.write("settings.txt", table.concat(lines, "\n") .. "\n"))
end
local savedSettings = mod.read("settings.txt")
if savedSettings then
    local character, completed, final, randomization, missions = savedSettings:match("^(%d+)\n(%d+)\n(%d+)\n(%d+)\n(.*)")
    if missions then
        commands.character = tonumber(character)
        commands.completed = tonumber(completed)
        commands.final = tonumber(final)
        commands.randomization = tonumber(randomization)
        local mission = 0
        for hidden, assignedCharacter in missions:gmatch("(%d+) (%d+)\n") do
            mission = mission + 1
            commands.missions[mission].hidden = tonumber(hidden)
            commands.missions[mission].character = tonumber(assignedCharacter)
        end
    end
end
function commands.receive(packet, bridge)
    local opcode, size = string.byte(packet, 1, 2)
    local accepted = #packet == size + 2
    local gameState = memory.u32(addresses.GAMESTATE)
    if accepted then
        if opcode == 0x01 and size == 2 then
            accepted = commands.gameReady(gameState)
            if accepted then
                local item = string.unpack("<I2", packet, 3)
                local amount = 1
                if item == 1 then
                    amount = 5
                elseif item >= 0x5D and item <= 0x6B then
                    amount = 3
                end
                local countAddress = gameState + addresses.ITEMCOUNT + item
                local count = memory.u8(countAddress)
                accepted = memory.set_u8(countAddress, (count + amount) & 255) == true
            end
        elseif opcode == 0x10 and size == 0 then
            accepted = commands.gameReady(gameState)
            if accepted then
                bridge.send(0x13, string.pack("<I4", bridge.commandSequence) .. bridge.session)
                for first = 1, #database.items, 84 do
                    local inventory = {string.char((first - 1) // 84)}
                    for index = first, math.min(first + 83, #database.items) do
                        local item = database.items[index]
                        local count = memory.u8(gameState + addresses.ITEMCOUNT + item)
                        inventory[#inventory + 1] = string.pack("<I2B", item, count)
                    end
                    bridge.send(0x11, table.concat(inventory))
                end
            end
        elseif opcode == 0x02 or opcode == 0x06 or opcode == 0x20 then
            for offset = 3, #packet, 2 do
                local mission, value = string.byte(packet, offset, offset + 1)
                if commands.missions[mission] then
                    if opcode == 0x20 then
                        commands.missions[mission].character = value
                    else
                        commands.missions[mission].hidden = value
                    end
                end
            end
            if opcode == 0x20 then
                commands.randomization = 1
            end
            saveSettings()
        elseif opcode == 0x03 or opcode == 0x04 or opcode == 0x05 or opcode == 0x21 then
            local names = {[0x03] = "character", [0x04] = "completed", [0x05] = "final", [0x21] = "randomization"}
            commands[names[opcode]] = string.byte(packet, 3)
            saveSettings()
        end
    end
    return accepted
end
return commands
