local addresses = require("addresses")
local chests = {}
local previousStates = {}
function chests.poll(bridge)
    if memory.loaded(2) then
        local objectTable = memory.u32(addresses.OBJECTTABLE)
        if objectTable ~= 0 then
            for module = 0, 31 do
                local pool = memory.u32(objectTable + addresses.MODULES + module * 4)
                if pool ~= 0 then
                    local kind = memory.u16(pool + addresses.MODULEKIND)
                    local stride = memory.u16(pool + addresses.MODULESTRIDE)
                    if kind == 0x0B and stride == 0x1BC then
                        local base = memory.u32(pool + addresses.MODULEBASE)
                        local count = memory.u16(pool + addresses.MODULECOUNT)
                        if base ~= 0 then
                            for slot = 0, count - 1 do
                                local chest = base + slot * stride
                                local state = memory.u8(chest + addresses.CHESTSTATE)
                                local flags = memory.u16(chest + addresses.OBJECTFLAGS)
                                local handler = memory.u32(chest + addresses.OBJECTHANDLER)
                                if state == 3 and flags ~= 0 and handler == addresses.CHESTHANDLER then
                                    if memory.u16(chest + addresses.CHESTKEY) ~= 0 then
                                        assert(memory.set_u16(chest + addresses.CHESTKEY, 0))
                                    end
                                end
                                if previousStates[chest] == 3 and state == 5 then
                                    local mission = memory.u16(addresses.MISSIONID)
                                    local chestSlot = memory.u8(chest + addresses.CHESTSLOT)
                                    bridge.send(0x08, string.char(mission, chestSlot))
                                end
                                previousStates[chest] = state
                            end
                        end
                    end
                end
            end
        end
    else
        previousStates = {}
    end
end
return chests
