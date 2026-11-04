local addresses = require("addresses")
local scaling = {}
local currentNode = 0
local currentIndex = 0
local previousCount = 0
local previousToken = 0
local previousWorld = 0
local scalePass = true
local function percentages(completed)
    local mission = memory.u16(addresses.MISSIONID)
    local relative = math.max(1, math.min(91, mission - completed))
    local progress = (relative - 1) / 90
    local hp, stats
    if progress <= 0.25 then
        hp = 100 - 4 * progress
        stats = 100 - 48 * progress
    elseif progress <= 0.5 then
        hp = 106 - 28 * progress
        stats = 124 - 144 * progress
    elseif progress <= 0.75 then
        hp = 126 - 68 * progress
        stats = 96 - 88 * progress
    else
        hp = 120 - 60 * progress
        stats = 90 - 80 * progress
    end
    return hp, stats
end
function scaling.poll(commands)
    if memory.loaded(107) then
        local manager = memory.u32(addresses.ENEMYMANAGER)
        if manager ~= 0 then
            local token = memory.u8(addresses.TRACKRECORD + addresses.SCANTOKEN)
            local world = memory.u8(addresses.WORLDRECORD + addresses.WORLDTOKEN)
            local count = memory.u32(manager + addresses.ENEMYLISTCOUNT)
            if token ~= previousToken or world ~= previousWorld then
                scalePass = true
                currentNode = 0
                currentIndex = 0
                previousToken = token
                previousWorld = world
            end
            if currentNode == 0 then
                currentNode = memory.u32(manager + addresses.ENEMYLISTHEAD)
            end
            if currentNode ~= manager + addresses.ENEMYLISTEND then
                local nextNode = memory.u32(currentNode + addresses.ENEMYNEXT)
                local slot = memory.u32(currentNode + addresses.ENEMYSLOT)
                local actor = 0
                if slot ~= 0 then
                    actor = memory.u32(slot)
                end
                if actor ~= 0 then
                    local flags = memory.u16(actor)
                    local kind = memory.u8(actor + addresses.ENEMYCLASS)
                    if (flags & 0x60) == 0x60 and scalePass and kind ~= 0x6B and kind ~= 0x32 then
                        local hpPercent, statPercent = percentages(commands.completed)
                        for index = 0, 7 do
                            local attackAddress = actor + addresses.ENEMYOFFENSE + 6 * index
                            local attack = memory.u16(attackAddress)
                            attack = math.max(5, math.floor(attack * statPercent / 100))
                            assert(memory.set_u16(attackAddress, attack))
                            local defenseAddress = actor + addresses.ENEMYDEFENSE + 2 * index
                            local defense = memory.u16(defenseAddress)
                            defense = math.max(5, math.floor(defense * statPercent / 100))
                            assert(memory.set_u16(defenseAddress, defense))
                        end
                        local hp = memory.u16(actor + addresses.ENEMYMAXHP)
                        hp = math.max(5, math.floor(hp * hpPercent / 100))
                        assert(memory.set_u16(actor + addresses.ENEMYMAXHP, hp))
                        assert(memory.set_u16(actor + addresses.ENEMYHP, hp))
                    end
                end
                currentNode = nextNode
                currentIndex = currentIndex + 1
            end
            if currentIndex == count then
                currentIndex = 0
                currentNode = 0
                scalePass = false
            end
            if count ~= previousCount then
                previousCount = count
                scalePass = true
                currentNode = 0
                currentIndex = 0
            end
        end
    end
end
return scaling
