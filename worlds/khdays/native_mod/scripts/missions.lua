local addresses = require("addresses")
local days = require("days")
local missions = {}
function missions.poll(commands)
    if memory.loaded(25) then
        local context = memory.u32(addresses.HOLOCONTEXT)
        if context ~= 0 then
            days.poll(commands, context)
            local page = memory.u32(context + addresses.PAGEA)
            if page ~= 0 then
                local manager = page + addresses.LISTMANAGER
                local mission = memory.u32(manager + addresses.LISTHEAD)
                local count = memory.u16(manager + addresses.LISTHEAD + addresses.LISTCOUNT)
                local visible = 0
                for _ = 1, count do
                    if mission ~= 0 then
                        local id = memory.u16(mission + addresses.NODEID)
                        local settings = commands.missions[id]
                        local hidden = settings and settings.hidden or 1
                        if memory.u32(mission + addresses.NODEHIDDEN) ~= hidden then
                            assert(memory.set_u32(mission + addresses.NODEHIDDEN, hidden))
                        end
                        if hidden == 0 then
                            visible = visible + 1
                        end
                        mission = memory.u32(mission + addresses.NODENEXT)
                    end
                end
                if memory.u16(manager + addresses.LISTVISIBLE) ~= visible then
                    assert(memory.set_u16(manager + addresses.LISTVISIBLE, visible))
                end
            end
        end
    end
end
return missions
