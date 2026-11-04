local addresses = require("addresses")
local field = {}
local missionResult = 0
local resultInitialized = false
local flashbacks = {[39] = true, [47] = true, [53] = true, [56] = true, [61] = true}
local denyTexts = {"No...", "Non...", "Nein ..."}
function field.character(commands, gameState)
    local scene = memory.u32(addresses.SCENEREC + addresses.SCENEID)
    if (scene == 2 or scene == 19) and memory.u32(addresses.SESSIONTAB) ~= 0 then
        local mission = memory.u16(addresses.MISSIONID)
        local character = commands.character
        if commands.randomization ~= 0 and commands.missions[mission] then
            character = commands.missions[mission].character
        end
        if flashbacks[mission] then
            character = 0
        end
        if memory.u32(addresses.SESSIONTAB + addresses.SESSIONKIND) ~= character then
            assert(memory.set_u32(addresses.SESSIONTAB + addresses.SESSIONKIND, character))
        end
        if memory.u8(addresses.MISSIONREC + addresses.MEMBERKIND) ~= character then
            assert(memory.set_u8(addresses.MISSIONREC + addresses.MEMBERKIND, character))
        end
        if character == 14 then
            local flags = memory.u8(gameState + addresses.XIONFLAGS)
            assert(memory.set_u8(gameState + addresses.XIONFLAGS, flags & 0xF7))
        end
    end
end
function field.startup(gameState)
    if memory.loaded(2) then
        local context = memory.u32(addresses.FIELDCONTEXT)
        local flags = memory.u32(gameState + addresses.GAMEFLAGS)
        local day = flags >> 23
        if context ~= 0 and day == 7 and memory.u16(context + addresses.FIELDACTIVE) == 0 then
            flags = (flags & ~(511 << 23)) | (357 << 23)
            assert(memory.set_u32(gameState + addresses.GAMEFLAGS, flags))
            assert(memory.set_u8(addresses.DAYCLOCK + addresses.CLOCKKIND, 0))
            assert(memory.set_u16(addresses.DAYCLOCK + addresses.CLOCKMINUTES, 0x2711))
            assert(memory.set_u16(addresses.DAYCLOCK + addresses.CLOCKELAPSED, 0))
            assert(memory.set_u32(addresses.SCENEREC + addresses.PENDINGID, 2))
            assert(memory.set_u32(addresses.SCENEREC + addresses.PENDINGARG, 0))
            local sceneObject = memory.u32(addresses.SCENEREC)
            if sceneObject ~= 0 then
                assert(memory.set_u32(sceneObject + addresses.SCENEOBJECTSTATE, 0xFFFFFFFE))
            end
        end
    end
end
function field.result(bridge, gameState)
    if memory.loaded(2) then
        local context = memory.u32(addresses.FIELDCONTEXT)
        if context ~= 0 then
            local total = memory.u32(context + addresses.MISSIONTOTAL)
            local done = memory.u32(context + addresses.MISSIONDONE)
            local goal = memory.u32(context + addresses.MISSIONGOAL)
            if total == 0 then
                missionResult = 0
            elseif done >= goal then
                missionResult = done == total and 2 or 1
            end
        end
    end
    local withdrawn = (memory.u8(gameState + addresses.WITHDRAWFLAGS) & 1) ~= 0
    if withdrawn then
        missionResult = 0
    end
    local flags = memory.u8(addresses.RESULTREC + addresses.RESULTFLAGS)
    if (flags & 1) == 0 then
        assert(memory.set_u8(addresses.RESULTREC + addresses.RESULTFLAGS, flags | 1))
        local mission = memory.u16(addresses.MISSIONID)
        if resultInitialized and not withdrawn and mission >= 1 and mission <= 91 then
            bridge.send(0x07, string.char(mission, missionResult))
        end
        missionResult = 0
    end
    resultInitialized = true
end
function field.gate(commands)
    if commands.final == 0 and memory.loaded(2) then
        local context = memory.u32(addresses.HUDCONTEXT)
        if context ~= 0 then
            local option = memory.u32(context + addresses.HUDSECONDENTRY)
            if option ~= 0 then
                local denied = false
                for _, text in ipairs(denyTexts) do
                    local matches = true
                    for index = 1, #text do
                        matches = matches and memory.u16(option + (index - 1) * 2) == string.byte(text, index)
                    end
                    denied = denied or matches
                end
                local cursor = memory.u32(context + addresses.HUDCURSOR)
                local count = memory.u32(context + addresses.HUDCOUNT)
                local state = memory.u32(context)
                if denied and cursor ~= 1 and count > 1 and state == 4 then
                    assert(memory.set_u32(context + addresses.HUDCURSOR, 1))
                end
            end
        end
    end
end
return field
