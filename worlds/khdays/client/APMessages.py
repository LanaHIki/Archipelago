import json
from NetUtils import JSONtoTextParser

MESSAGE_OPCODE = 0x23
MAX_MESSAGE_PART_BYTES = 254
FIRST_MESSAGE_PART = 1
LAST_MESSAGE_PART = 2


class MessageText(JSONtoTextParser):
    def __call__(self, messageNodes):
        self.messageParts = []
        for messageNode in messageNodes:
            self.handle_node(messageNode)
        return self.messageParts

    def _handle_text(self, messageNode):
        self.messageParts.append({"text": messageNode.get("text", ""), "color": "#ebf1f8"})
        return ""

    def _handle_color(self, messageNode):
        textColor = "#ebf1f8"
        for colorName in messageNode.get("color", "white").split(";"):
            if colorName in self.color_codes:
                textColor = "#" + self.color_codes[colorName]
        if messageNode.get("type") in ("player_id", "player_name"):
            textColor = "#9cdcff"
        self.messageParts.append({"text": messageNode.get("text", ""), "color": textColor})
        return ""


def messagePacket(message):
    messageBytes = json.dumps(message, ensure_ascii=False).encode("utf-8")
    packet = bytearray()
    for messageOffset in range(0, len(messageBytes), MAX_MESSAGE_PART_BYTES):
        messagePart = messageBytes[messageOffset:messageOffset + MAX_MESSAGE_PART_BYTES]
        partFlags = 0
        if messageOffset == 0:
            partFlags = FIRST_MESSAGE_PART
        if messageOffset + len(messagePart) == len(messageBytes):
            partFlags = partFlags | LAST_MESSAGE_PART
        partPayload = bytes([partFlags]) + messagePart
        packet.extend(bytes([MESSAGE_OPCODE, len(partPayload)]))
        packet.extend(partPayload)
    return packet
