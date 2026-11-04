from kivy.metrics import dp
from kivymd.uix.button import MDButton, MDButtonText
from kivy.uix.button import Button
from kvui import GameManager
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.checkbox import CheckBox
import asyncio
from worlds.khdays import KHDaysWorld
from worlds.khdays.client.WorldLocations import mission_locations
from worlds.khdays.Items import Character_Table
from kivy.uix.boxlayout import BoxLayout
from worlds.khdays.Options import goalChoice, charRando
from ..Names import LocationName, ItemName
from collections import Counter
from worlds.khdays.Rules import RulesChests, RulesBosses, RulesMissions

class DaysUI(GameManager):
    def build(self):
        layout = super().build()
        melonMixConnectbutton = MDButton(
            MDButtonText(text="MelonMix"),
            style="filled",
            radius = 5,
            theme_width="Primary",
            theme_height="Custom",
            size_hint_x=None,
            size_hint_y=None,
            height = dp(30),
            pos_hint={"center_y": 0.55},
        )
        self.buildNewTab()
        self.buildCharacterSelectTab()
        self.server_connect_button.disabled = True
        melonMixConnectbutton.bind(on_press=self.link)
        self.connect_layout.add_widget(melonMixConnectbutton)
        return layout

    def link(self, button):
        self.commandprocessor._cmd_tcpconnect()
        self.server_connect_button.disabled = False

    def buildNewTab(self):
        self.checks = None
        self.list = GridLayout(cols=1, size_hint_y=None, spacing = 10)
        self.list.bind(minimum_height=self.list.setter("height"))

        scroll = ScrollView()
        scroll.add_widget(self.list)
        panel = BoxLayout(orientation="vertical")

        bar = BoxLayout(
            size_hint_y=None,
            height=dp(30),
            spacing=dp(5),
            padding=dp(5),
        )
        
        bar.add_widget(Label(text="Checklist options"))
        self.missionsDoneText = Label(text = "Mission Completes Needed = ")
        self.debugButton = Button(text="get Debug Bundle", on_press=lambda button: asyncio.create_task(self.ctx.printDebug()))
        bar.add_widget(self.missionsDoneText)
        bar.add_widget(self.debugButton)
        panel.add_widget(bar)
        panel.add_widget(scroll)
        self.add_client_tab("Checklist", panel)

        Clock.schedule_interval(self.refresh, 1)

    def buildCharacterSelectTab(self):
        self.characterList = GridLayout(cols=1,spacing = 10, size_hint_y = None)
        self.characterList.bind(minimum_height=self.characterList.setter("height"))
        scroll = ScrollView()
        scroll.add_widget(self.characterList)
        self.buildButtons = []
        self.add_client_tab("Character Select",scroll)

        Clock.schedule_interval(self.characterSelect,1)


    def characterSelect(self,dt):
        for name, charData in Character_Table.items():
            if charData.khDaysID in self.ctx.characterUnlocked and charData.khDaysID not in self.buildButtons:
                buttonRow = Button(text=name,on_press=lambda button, char=charData.khDaysID: asyncio.create_task(self.ctx.chooseChar(char)), size_hint_y = None, height = dp(40))
                self.characterList.add_widget(buttonRow)
                self.buildButtons.append(charData.khDaysID)

    #this is growing out of control as well
    def refresh(self, dt):
        done = self.ctx.checked_locations
        allids = self.ctx.server_locations
        unlocked = self.ctx.misionUnlocked
        localLocationRules = InventoryChecks(self.ctx)
        state = (
            frozenset(done),
            frozenset(allids),
            frozenset(unlocked),
            frozenset(localLocationRules.currentInventoryCounts.items()),
        )
        if self.ctx.goalChoice == goalChoice.option_Mission_Completed:
            needed = 64 - len(self.ctx.completed)
            if needed < 0:
                needed = 0
            self.missionsDoneText.text = "Mission Completes Needed = " + str(needed)
        if self.ctx.goalChoice == goalChoice.option_SeaSalt_Icecream:
                    needed = self.ctx.seaRequired - self.ctx.seaSaltGotten
                    if needed < 0:
                        needed = 0
                    self.missionsDoneText.text = "Sea Salt Icecreams Needed = " + str(needed)
        if state != self.checks:
            self.checks = state
            self.list.clear_widgets()

            for mission, checks in mission_locations.items():
                if mission in unlocked:
                    for name in checks:
                        available = True
                        if name in localLocationRules.locationRules:
                            available = localLocationRules.locationRules[name](localLocationRules, self.ctx.slot)
                        loc = KHDaysWorld.location_name_to_id[name]
                        if loc in allids and loc not in done and available:
                            row = Label(
                                text=name,
                                size_hint_y=None,
                                height=dp(30),
                                halign="left",
                                valign="middle",
                            )
                            row.bind(size=row.setter("text_size"))
                            self.list.add_widget(row)


class InventoryChecks:
    def __init__(self, ctx):
        self.currentInventoryCounts = Counter(item.item for item in ctx.items_received)
        self.chestChecks = RulesChests()
        self.bossChecks = RulesBosses()
        self.missionChecks = RulesMissions()
        if ctx.charRando == charRando.option_Per_Mission_Rando:
            self.missionChecks.mission4Character = ctx.missionChars["4"]
        self.locationRules = {
            LocationName.Mission4Clear: self.missionChecks.mission4Check,
            LocationName.Mission4Clear2: self.missionChecks.mission4Check,
            LocationName.Mission4Clear3: self.missionChecks.mission4Check,
            LocationName.Mission10Clear: self.missionChecks.mission10Check,
            LocationName.Mission10Clear2: self.missionChecks.mission10Check,
            LocationName.Mission10Clear3: self.missionChecks.mission10Check,
            LocationName.Mission71Clear: self.missionChecks.mission71Check,
            LocationName.Mission71Clear2: self.missionChecks.mission71Check,
            LocationName.Mission71Clear3: self.missionChecks.mission71Check,
            LocationName.Mission32Clear: self.bossChecks.antlionCheck,
            LocationName.Mission32Clear2: self.bossChecks.antlionCheck,
            LocationName.Mission32Clear3: self.bossChecks.antlionCheck,
            LocationName.Mission50Clear: self.bossChecks.infernalEngineCheck,
            LocationName.Mission50Clear2: self.bossChecks.infernalEngineCheck,
            LocationName.Mission50Clear3: self.bossChecks.infernalEngineCheck,
            LocationName.Mission61Clear: self.bossChecks.guardArmorCheck,
            LocationName.Mission61Clear2: self.bossChecks.guardArmorCheck,
            LocationName.Mission61Clear3: self.bossChecks.guardArmorCheck,
            LocationName.Mission66Clear: self.bossChecks.leechgraveCheck,
            LocationName.Mission66Clear2: self.bossChecks.leechgraveCheck,
            LocationName.Mission66Clear3: self.bossChecks.leechgraveCheck,
            LocationName.Mission69Clear: self.bossChecks.crimsonPranksterCheck,
            LocationName.Mission69Clear2: self.bossChecks.crimsonPranksterCheck,
            LocationName.Mission69Clear3: self.bossChecks.crimsonPranksterCheck,
            LocationName.Mission78Clear: self.bossChecks.rulerOfTheSkyCheck,
            LocationName.Mission78Clear2: self.bossChecks.rulerOfTheSkyCheck,
            LocationName.Mission78Clear3: self.bossChecks.rulerOfTheSkyCheck,
            LocationName.Mission90Clear: self.bossChecks.xionCheck,
            LocationName.Mission90Clear2: self.bossChecks.xionCheck,
            LocationName.Mission90Clear3: self.bossChecks.xionCheck,
            LocationName.Mission91Clear: self.bossChecks.saixCheck,
            LocationName.Mission91Clear2: self.bossChecks.saixCheck,
            LocationName.Mission91Clear3: self.bossChecks.saixCheck,
            LocationName.Mission15Chest2: self.chestChecks.argrabahRoofCheck,
            LocationName.Mission16Chest2: self.chestChecks.argrabahRoofCheck,
            LocationName.Mission19Chest0: self.chestChecks.argrabahRoofCheck,
            LocationName.Mission32Chest2: self.chestChecks.argrabahRoofCheck,
            LocationName.Mission34Chest0: self.chestChecks.argrabahRoofCheck,
            LocationName.Mission48Chest7: self.chestChecks.caveHiChest,
            LocationName.Mission48Chest5: self.chestChecks.caveHiBackChest,
            LocationName.Mission51Chest7: self.chestChecks.aliceHedgeCheck,
            LocationName.Mission55Chest4: self.chestChecks.aliceHedgeCheck,
            LocationName.Mission59Chest2: self.chestChecks.twilightRoofCheck,
            LocationName.Mission67Chest4: self.chestChecks.aliceHedgeCheck,
            LocationName.Mission68Chest3: self.chestChecks.caveHiBackChest,
            LocationName.Mission82Chest1: self.chestChecks.argrabahRoofCheck,
            LocationName.Mission90Chest2: self.chestChecks.secretDepthsChestCheck,
        }

    def has(self, name, player, count=1):
        item = KHDaysWorld.item_name_to_id[name]
        return self.currentInventoryCounts[item] >= count

    def has_any(self, names, player):
        return any(self.has(name, player) for name in names)
