local addresses = require("addresses")
local days = {}
function days.poll(commands, context)
    local page = memory.u32(context + addresses.PAGEB)
    if memory.u32(addresses.PAGEBKIND) == 5 and page ~= 0 then
        local rows = memory.u32(page + addresses.DAYROWS)
        if memory.u32(page) > 0 and rows ~= 0 then
            local count = 0
            local changed = false
            for index = 0, 54 do
                local entry = addresses.DAYTABLE + index * addresses.DAYTABLESTRIDE
                local firstDay = memory.u16(entry)
                local lastDay = memory.u16(entry + addresses.DAYTABLESTRIDE) - 1
                local visible = false
                for _, settings in ipairs(commands.missions) do
                    visible = visible or (settings.hidden == 0 and settings.day >= firstDay and settings.day <= lastDay)
                end
                if visible then
                    local name = memory.u32(page + addresses.DAYSTRINGS)
                    local nameIndex = memory.u16(entry + addresses.DAYTABLENAME)
                    for _ = 1, nameIndex do
                        name = name + memory.u32(name)
                    end
                    local row = rows + count * addresses.DAYROWSTRIDE
                    if memory.u32(row) ~= firstDay or memory.u32(row + addresses.DAYROWLAST) ~= lastDay or memory.u32(row + addresses.DAYROWNAME) ~= name + 4 then
                        assert(memory.set_u32(row, firstDay))
                        assert(memory.set_u32(row + addresses.DAYROWLAST, lastDay))
                        assert(memory.set_u32(row + addresses.DAYROWNAME, name + 4))
                        changed = true
                    end
                    count = count + 1
                end
            end
            if changed or memory.u32(page + addresses.DAYCOUNT) ~= count then
                local knobHeight = math.max(32, math.min(160, 1600 // math.max(1, count)))
                assert(memory.set_u32(page + addresses.DAYCOUNT, count))
                assert(memory.set_u32(page + addresses.DAYCURSOR, 0))
                assert(memory.set_u32(page + addresses.DAYSCROLL, 0))
                assert(memory.set_u32(page + addresses.DAYPREVIOUSSCROLL, 0))
                assert(memory.set_u32(page + addresses.DAYSCROLLMAX, math.max(0, count - 10) * 16))
                assert(memory.set_u32(page + addresses.DAYKNOB, 0))
                assert(memory.set_u32(page + addresses.DAYKNOBHEIGHT, knobHeight))
                assert(memory.set_u32(page + addresses.DAYKNOBMAX, 160 - knobHeight))
                assert(memory.set_u32(page + addresses.DAYROWSDIRTY, 1))
                assert(memory.set_u32(page + addresses.DAYMARKERSDIRTY, 1))
                assert(memory.set_u32(page + addresses.DAYLAYOUTDIRTY, 1))
            end
        end
    end
end
return days
