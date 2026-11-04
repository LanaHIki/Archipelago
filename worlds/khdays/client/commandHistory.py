from CommonClient import CommonContext, ClientCommandProcessor, ClientStatus
from MultiServer import mark_raw
import asyncio
import copy
from worlds.khdays import KHDaysWorld
from worlds.khdays.client.WorldLocations import mission_locations
from pathlib import Path
import Utils
from zipfile import ZipFile, ZIP_DEFLATED
from ..Options import charRando, goalChoice
from ..Items import Bundles, item_dictionary_table
from .NativeBridge import NativeBridge
from .APMessages import MessageText, messagePacket
class Commands(ClientCommandProcessor):  
    @mark_raw
    def _cmd_native(self, directory=""):
        """Connect to the Lua mod: /native <port saves/mods/archipelago.khdays directory>."""
        if directory:
            asyncio.create_task(self.connect(directory.strip().strip('"')))

    @mark_raw
    def _cmd_tcp(self, text=""):
        """Send hex bytes to MelonMix, such as /tcp 48 26."""
        if text:
            asyncio.create_task(self.send(text))
    def _cmd_tcpconnect(self):
        asyncio.create_task(self.connect());

    def _cmd_character(self,text = ""):
        character = int(text)
        if character in self.ctx.characterUnlocked:
            self.ctx.chosenChar = character
            asyncio.create_task(self.ctx.chooseChar(character))

    def _cmd_unlock_character(self,text = ""):
        character = int(text)
        asyncio.create_task(self.ctx.unlock_character(character))

    def _cmd_give_item(self, text = ""):
        item = int(text)
        asyncio.create_task(self.ctx.sendItem(item))
        
    def _cmd_unlock_mission(self,text = ""):
        if text:
            asyncio.create_task(self.ctx.unlock_mission(int(text)))
            asyncio.create_task(self.ctx.sendTable())


    async def send(self, text):
        try:
            await self.ctx.send(None, bytes.fromhex(text))
        except ValueError:
            self.output("Use hex bytes, such as /tcp 48 26")
    async def listen(self, reader):
        try:
            while True:
                read = await reader.readexactly(1)
                opcode = int.from_bytes(read, "little")
                read = await reader.readexactly(1)
                size = int.from_bytes(read,"little")
                data = await reader.readexactly(size)
                await self.ctx.command_handeling(opcode, data)
        except (asyncio.IncompleteReadError, OSError, ValueError) as err:
            self.output(f"Couldn't open new client: {err}")
        finally:
            self.ctx.streams[1].close()
            self.ctx.streams = None
            self.ctx.connectionStatus = False

    async def connect(self, native_directory=None):
        try:
            if self.ctx.streams is not None:
                self.ctx.streams[1].close()
                await self.ctx.task
            if native_directory is None:
                self.ctx.streams = await asyncio.open_connection("127.0.0.1", 43050)
            else:
                bridge = NativeBridge(native_directory)
                await asyncio.wait_for(bridge.wait_for_acknowledgement(), timeout=30)
                self.ctx.streams = bridge, bridge
            reader,writer = self.ctx.streams
            self.ctx.task = asyncio.create_task(self.listen(reader))
            self.ctx.connectionStatus = True
            if self.ctx.ui is not None:
                self.ctx.ui.server_connect_button.disabled = False

            asyncio.create_task(self.ctx.recheckMissions())
            asyncio.create_task(self.ctx.sendTable())
            asyncio.create_task(self.ctx.syncInventory())
            if self.ctx.charRando == charRando.option_Per_Mission_Rando:
                asyncio.create_task(self.ctx.sendCharTable())
            asyncio.create_task(self.ctx.sendCharRandoSetting())

            
            self.output("Native Lua mod connected" if native_directory else "Melonmix Connected")
            if self.ctx.chosenChar is not None:
                asyncio.create_task(self.ctx.chooseChar(self.ctx.chosenChar))

        except (TimeoutError, OSError) as err:
            self.output(f"error: {err}")


class DaysContext(CommonContext):
        command_processor = Commands
        game = None
        items_handling = 0b111
        want_slot_data = True

        #todo rewrite
        def on_print(self, args):
            super().on_print(args)
            asyncio.create_task(self.sendAPMessage({"text": args["text"]}))

        def on_print_json(self, args):
            super().on_print_json(args)
            parts = self.messageText(copy.deepcopy(args["data"]))
            asyncio.create_task(self.sendAPMessage({"parts": parts}))

        async def sendAPMessage(self, message):
            if self.streams is not None and not isinstance(self.streams[1], NativeBridge):
                await self.send(None, messagePacket(message))

        async def server_auth(self, password_requested=False):
            if password_requested and not self.password:
                await super().server_auth(password_requested)

            await self.get_username()
            await self.send_connect()

        def on_package(self, cmd, args):
            if cmd == "Connected":
                #oh god it's growing, make different functions
                self.slot_data = args["slot_data"]
                self.starting_mission = self.slot_data["starting_mission"]
                self.chosenChar = self.slot_data["starting_character"]
                self.scan = self.slot_data["Starting Inventory"]
                self.charRando = self.slot_data["charrando"]
                self.goalChoice = self.slot_data["Goal Choice"]
                if self.goalChoice == goalChoice.option_SeaSalt_Icecream:
                    self.seaRequired = self.slot_data["Sea Salt Required"]                
                if self.charRando == charRando.option_Per_Mission_Rando:
                    self.missionChars = self.slot_data["missionSetRando"]
                if self.chosenChar not in self.characterUnlocked:
                    self.characterUnlocked.append(self.chosenChar)
                if self.streams is not None:
                    asyncio.create_task(self.chooseChar(self.chosenChar))
                if self.starting_mission not in self.misionUnlocked:
                    self.misionUnlocked.append(self.starting_mission)
                if self.streams is not None:
                    asyncio.create_task(self.sendTable())
                    if self.charRando == charRando.option_Per_Mission_Rando:
                        asyncio.create_task(self.sendCharTable())
                    asyncio.create_task(self.sendCharRandoSetting())

            elif cmd == "ReceivedItems":
                asyncio.create_task(self.syncInventory())
                asyncio.create_task(self.recheckMissions())

        #old doesn't get used
        async def give_items(self):
            async with self.item_lock:
                while (
                    self.streams is not None
                    and self.item_index < len(self.items_received)
                ):
                    item = self.items_received[self.item_index]
                    data = self.slot_data["items"][str(item.item)]

                    if data["mission"] == False and data["character"] == False:
                        await self.sendItem(data["id"])
                    elif data["mission"] == True:
                        await self.unlock_mission(data["id"])
                        await self.sendTable()
                    elif data["character"] ==True:
                        await self.unlock_character(data["id"])                    
                    self.item_index += 1


        def __init__(self, *args):
            super().__init__(*args)
            self.messageText = MessageText(self)
            self.task = None
            self.streams = None
            self.connectionStatus = False
            self.sendLock = asyncio.Lock()
            self.completed = set()
            self.slot_data = {}
            self.chosenChar = None;
            self.inventoryDone = asyncio.Event()
            self.inventoryQuery = None
            self.completedInventoryQuery = None
            self.starting_mission = None
            self.inventory = {}
            self.debugAPLedger = []
            self.parts = set()
            self.sendingDone = False
            self.item_index = 0
            self.item_lock = asyncio.Lock()
            self.output_dir = Path(Utils.user_path("khDays", "debug-bundles")).expanduser().resolve()
            self.debugInventory = []
            self.debugReceived = []
            self.debugMyChests =[]
            self.debugMyMissions = []
            self.debugMissionLocations = []
            self.debugChestLocations = []
            self.misionUnlocked = []
            self.goalChoice = []
            self.saltRequired = []
            self.characterUnlocked = []
            self.seaRequired = 0
            self.ledgerPos  = 0
            self.seaSaltGotten = 0
            self.charRando = charRando.option_Full_Character_Rando

        async def shutdown(self):
            if self.streams is not None:
                self.streams[1].close()
            if self.task is not None:
                await self.task
            await super().shutdown()

        

        async def sendItem(self, item: int):
            await self.send(0x01, item.to_bytes(2, "little"))

            
        async def askInv(self):
            await self.send(0x10)

        async def checkItemsAndSend(self):
            itemCounts = {}
            bundleStagesReceived = {}
            
            #debug code for writign things down
            for item in self.items_received[self.ledgerPos:]:
                name = self.item_names.lookup_in_slot(item.item, self.slot)
                check = self.location_names.lookup_in_slot(item.location, item.player)
                player = self.player_names[item.player]
                entry = {"itemName": name, "location": check, "player": player}
                self.debugAPLedger.append(entry)
                self.ledgerPos += 1
            
            #split this into more functions later
            #mission character first
            currentSeaSalt = 0
            #kinda realise this is unreadable at first, gotta make this more clear
            for item in self.items_received:
                data = self.slot_data["items"][str(item.item)]
                key = data["id"]

                if data["mission"]:
                    await self.unlock_mission(key)
                elif data["character"]:
                    if key not in self.characterUnlocked:
                        await self.unlock_character(key)
                elif data["seaSalt"]:
                    currentSeaSalt += 1
                elif data.get("pack", False):
                    bundleName = self.item_names.lookup_in_slot(item.item, self.slot)
                    if bundleName in self.slot_data["gear_bundles"]:
                        bundleStages = self.slot_data["gear_bundles"][bundleName]
                    else:
                        bundleStages = Bundles[bundleName]
                    bundleID = data["id"]
                    bundleStageIndex = bundleStagesReceived.get(bundleID, 0) if len(bundleStages) > 1 else 0
                    bundleStagesReceived[bundleID] = bundleStageIndex + 1
                    if bundleStageIndex < len(bundleStages):
                        for bundledItemName, bundledItemCount in bundleStages[bundleStageIndex].items():
                            bundledItemID = item_dictionary_table[bundledItemName].khDaysID
                            itemCounts[bundledItemID] = itemCounts.get(bundledItemID, 0) + bundledItemCount
                else:
                    itemCounts[key] = itemCounts.get(key, 0) + 1

            await self.sendTable()

            if self.goalChoice == goalChoice.option_SeaSalt_Icecream:
                await self.seaSaltUpdate(currentSeaSalt)

            #now items replay
            self.debugInventory.append(self.inventory.copy())
            self.debugReceived.append(itemCounts)                
            for item, apAmount in itemCounts.items():
                amount = self.inventory[item]
                magic = 0x5D <= item <= 0x6B
                if magic:
                    amountNeeded = apAmount - (amount // 3)
                elif item == 0x01:
                    amountNeeded = apAmount - (amount // 5)
                else:
                    amountNeeded = apAmount - amount
                
                if amountNeeded < 0:
                    amountNeeded = 0
                for amountLoop in range(amountNeeded):
                    await self.sendItem(item)

        #need to check if everything needs to be async def or not
        async def seaSaltUpdate(self, seaSaltGotten : int):
            self.seaSaltGotten = seaSaltGotten
            await self.goalCheck()
        async def syncInventory(self):
            async with self.item_lock:
                if self.streams is not None and self.slot_data:
                    streams = self.streams
                    self.inventoryDone.clear()
                    await self.askInv()
                    received = False
                    if isinstance(streams[0], NativeBridge):
                        expectedInventoryQuery = streams[0].session, streams[0].last_inventory_query_sequence
                        while self.streams is streams and self.completedInventoryQuery != expectedInventoryQuery:
                            await asyncio.sleep(0.05)
                        received = self.streams is streams and self.sendingDone
                    else:
                        try:
                            await asyncio.wait_for(self.inventoryDone.wait(), timeout=5)
                            received = True
                        except asyncio.TimeoutError:
                            pass
                    if received:
                        await self.checkItemsAndSend()
                        await self.askInv()
        async def game_completed(self):
            if not self.finished_game:
                self.finished_game = True
                await self.send_msgs([{
                    "cmd": "StatusUpdate",
                    "status": ClientStatus.CLIENT_GOAL
                }])

        async def unlock_mission(self, mission : int):
            if mission not in self.misionUnlocked:
                self.misionUnlocked.append(mission)

        async def command_handeling(self,opcode,data):
            if opcode == 0x13:
                self.inventoryQuery = data[4:].decode("ascii"), int.from_bytes(data[:4], "little")
            elif opcode == 0x12:
                asyncio.create_task(self.syncInventory())
            elif(opcode == 0x07) :
               await self.mission_cleared(data)
            elif(opcode == 0x08):
                await self.chest_opened(data)
            elif(opcode == 0x09):
                await self.game_completed()
            elif(opcode == 0x11):
                inventorySlot = data[0]
                if inventorySlot == 0:
                    self.inventory.clear()
                    self.sendingDone = False

                for itemPos in range(1, len(data), 3):
                    itemAmount = itemPos + 2
                    item = int.from_bytes(data[itemPos:itemAmount], "little")
                    self.inventory[item] = data[itemAmount]

                if inventorySlot == 3:
                    self.sendingDone = True
                    self.completedInventoryQuery = self.inventoryQuery
                    self.inventoryDone.set()
                    print(self.inventory)
        
        async def unlock_character(self, character : int):
            self.characterUnlocked.append(character)

        async def sendTable(self):
            data = bytearray()
            for mission in range(1, 92):
                locked = int(mission not in self.misionUnlocked)
                data.extend([mission, locked])
            await self.send(0x06, data)


        async def sendCharTable(self):
            data = bytearray()
            for mission in range(1,92):
                character = self.missionChars[str(mission)]
                data.extend([mission,character])
            await self.send(0x20,data)
        
        async def chooseChar(self, character: int):
            await self.send(0x03, character.to_bytes(1, "little"))

        async def mission_cleared(self, data):
            mission = data[0]
            result = data[1]

            
            checks = mission_locations[mission]
            locations = []
            self.debugMyMissions.append([mission,result])
            for name, check in checks.items():
                if check.kind == "Clear":
                    locations.append(KHDaysWorld.location_name_to_id[name])
            
            self.debugMissionLocations.append(locations)
            await self.check_locations(locations)
            self.completed.add(mission)
            await self.sendDone()

        async def recheckMissions(self):
            for mission, checks in mission_locations.items():
                for name, check in checks.items():
                    if check.kind == "Clear":
                        loc = KHDaysWorld.location_name_to_id[name]
                        if loc in self.checked_locations:
                            self.completed.add(mission)
            await self.sendDone()

        async def sendDone(self):
            done = len(self.completed)
            await self.send(0x04, bytes([done]))
            await self.goalCheck()

        async def goalCheck(self):
            if self.goalChoice == goalChoice.option_Mission_Completed:
                if len(self.completed) >= 64:
                    await self.send(0x05, bytes([1]))
            elif self.goalChoice == goalChoice.option_SeaSalt_Icecream:
                if self.seaSaltGotten >= self.seaRequired:
                    await self.send(0x05,bytes([1]))
        async def chest_opened(self, data):
            mission = data[0]
            slot = data[1]
            checks = mission_locations[mission]
            locations = []
            self.debugMyChests.append([mission,slot])
            for name, check in checks.items():
                if check.kind == "Chest" and check.slot == slot:
                    locations.append(KHDaysWorld.location_name_to_id[name])
            self.debugChestLocations.append(locations)
            await self.check_locations(locations)

        async def sendCharRandoSetting(self):
            await self.send(0x21,bytes([self.charRando]))
        async def send(self, opcode, data=b""):
            async with self.sendLock:
                if self.streams is not None:
                    #need to change this once /tcp is no longer needed
                    packet = data if opcode is None else bytes([opcode, len(data)]) + data
                    writer = self.streams[1]
                    try:
                        writer.write(packet)
                        await asyncio.wait_for(writer.drain(), timeout=5)
                    except (asyncio.TimeoutError, ConnectionResetError) as err:
                        self.command_processor(self).output(f"Error as {err}")

        async def printDebug(self):
            self.output_dir.mkdir(parents = True, exist_ok= True)
            with open(self.output_dir / "Received_items_history.txt", "w", encoding="utf=8") as file:
                print(self.debugReceived,file=file)
            with open(self.output_dir / "item_inventory_snapshot_history.txt", "w", encoding="utf=8") as file:
                print(self.debugInventory,file=file)
            with open(self.output_dir / "chest_locations_send_history.txt", "w", encoding="utf=8") as file:
                print(self.debugChestLocations,file=file)
            with open(self.output_dir / "mission_locations_send_history.txt", "w", encoding="utf=8") as file:
                print(self.debugMissionLocations,file=file)
            with open(self.output_dir / "apLedger_History.txt", "w", encoding="utf=8") as file:
                print(self.debugAPLedger,file=file)
            with open(self.output_dir / "repored_chest_slots.txt", "w", encoding="utf=8") as file:
                print(self.debugMyChests,file=file)
            with open(self.output_dir / "reported_mission_slots.txt", "w", encoding="utf=8") as file:
                print(self.debugMyMissions,file=file)
            
            with ZipFile(self.output_dir / "Debug.zip","w", compression=ZIP_DEFLATED) as zip:
                zip.write(self.output_dir / "Received_items_history.txt", arcname= "Received_items_history.txt")
                zip.write(self.output_dir / "item_inventory_snapshot_history.txt", arcname= "item_inventory_snapshot_history.txt")
                zip.write(self.output_dir / "chest_locations_send_history.txt", arcname= "chest_locations_send_history.txt")
                zip.write(self.output_dir / "mission_locations_send_history.txt", arcname= "mission_locations_send_history.txt")
                zip.write(self.output_dir / "apLedger_History.txt", arcname= "apLedger_History.txt")
                zip.write(self.output_dir / "repored_chest_slots.txt", arcname= "repored_chest_slots.txt")
                zip.write(self.output_dir / "reported_mission_slots.txt", arcname= "reported_mission_slots.txt")
