local bridge = {}
local session = ""
local commandAcknowledged = 0
local eventSequence = 0
local events = {}
local lastIncoming
local outputChanged = false
local function hexadecimal(packet)
    return (packet:gsub(".", function(character)
        return string.format("%02x", string.byte(character))
    end))
end
local function bytes(packet)
    return (packet:gsub("%x%x", function(pair)
        return string.char(tonumber(pair, 16))
    end))
end
local function publish()
    local lines = {session, tostring(commandAcknowledged), tostring(eventSequence)}
    for _, event in ipairs(events) do
        lines[#lines + 1] = event.sequence .. " " .. event.packet
    end
    return mod.write("game.txt", table.concat(lines, "\n") .. "\n")
end
local saved = mod.read("game.txt")
if saved then
    session, commandAcknowledged, eventSequence = saved:match("^([^\n]*)\n(%d+)\n(%d+)\n")
    commandAcknowledged = tonumber(commandAcknowledged) or 0
    eventSequence = tonumber(eventSequence) or 0
    session = session or ""
    for sequence, packet in saved:gmatch("\n(%d+) (%x+)") do
        events[#events + 1] = {sequence = tonumber(sequence), packet = packet}
    end
end
function bridge.send(opcode, payload)
    eventSequence = eventSequence + 1
    local packet = string.char(opcode, #payload) .. payload
    events[#events + 1] = {sequence = eventSequence, packet = hexadecimal(packet)}
    outputChanged = true
end
function bridge.poll(handleCommand)
    local incoming = mod.read("client.txt")
    if incoming and incoming ~= lastIncoming then
        local incomingSession, eventAcknowledged = incoming:match("^([%w]+)\n(%d+)\n")
        if incomingSession then
            if incomingSession ~= session then
                session = incomingSession
                commandAcknowledged = 0
                for index, event in ipairs(events) do
                    event.sequence = index
                end
                eventSequence = #events
            end
            eventAcknowledged = tonumber(eventAcknowledged)
            bridge.session = session
            while events[1] and events[1].sequence <= eventAcknowledged do
                table.remove(events, 1)
            end
            for sequence, packet in incoming:gmatch("\n(%d+) (%x+)") do
                local commandSequence = tonumber(sequence)
                if commandSequence == commandAcknowledged + 1 then
                    bridge.commandSequence = commandSequence
                    if handleCommand(bytes(packet)) then
                        commandAcknowledged = commandSequence
                    end
                    break
                end
            end
            outputChanged = true
            local lastCommand = tonumber(incoming:match("\n(%d+) %x+\n$"))
            if not lastCommand or lastCommand == commandAcknowledged then
                lastIncoming = incoming
            end
        end
    end
    if outputChanged then
        outputChanged = not publish()
    end
end
return bridge
