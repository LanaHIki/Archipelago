from BaseClasses import Tutorial, ItemClassification
from Fill import fast_fill
from Utils import local_path
from worlds.LauncherComponents import Component, components, Type, launch as run_client
from worlds.AutoWorld import World, WebWorld
from .Items import *
from .Locations import *
from .Names import RegionName
from .Names import ItemName
from .Names import LocationName
from .Regions import create_region, connect_regions
from .Rules import *
from .Options import DaysOpts, charRando,goalChoice, startingCharacter

def launch():
    from runpy import run_module
    run_module("worlds.khdays.client.KHDaysClient", run_name="__main__")

def start():
    run_client(launch, name="KH Days Client")

components.append(Component("KH Days Client", func=start, component_type=Type.CLIENT, game_name="KH Days"))

class KHDaysWorld(World):
    game = "KH Days"
    options_dataclass = DaysOpts
    item_name_to_id = {item: item_id for item_id, item in enumerate(V2Items.keys(), 0x250000000)}
    location_name_to_id = {name: daysLocation.locationID for name,daysLocation in all_locations.items()}

    def __init__(self,multiworld: "MultiWorld", player: int):
        super().__init__(multiworld,player)

    def create_item(self,name: str) -> Item:
        if name in V2Prog:
            item_classification = ItemClassification.progression
        elif name in V2Useful:
            item_classification = ItemClassification.useful
        else:
            item_classification = ItemClassification.filler

        created_item = DaysItem(name,item_classification, self.item_name_to_id[name],self.player)

        return created_item
    def generate_early(self):
        available_gears = []
        self.gear_bundles = {'Progressive Gear': []}
        for tier_name, tier_gears in GearTiers.items():
            available_gears.extend(tier_gears)
            for gear_count in GearDraws[tier_name]:
                chosen_gears = self.random.sample(available_gears, gear_count)
                for gear_name in chosen_gears:
                    available_gears.remove(gear_name)
                self.gear_bundles['Progressive Gear'].append(dict.fromkeys(chosen_gears, 1))
        if self.options.goalchoice == goalChoice.option_SeaSalt_Icecream:
            seaSaltRequired = self.options.seasaltrequired.value
            seaSaltPool = self.options.seasaltpool.value
            if seaSaltRequired > seaSaltPool:
                raise ValueError(f"Icecream required ({seaSaltRequired}) exceeds pool ({seaSaltPool})")

    #need to organize this cuz it's just growing
    def create_items(self) -> None:
        self.item_quantity_dict = {
            name: data.quantity
            for name, data in V2Items.items()
        }
        #seasalt
        if self.options.goalchoice == goalChoice.option_SeaSalt_Icecream:
            self.item_quantity_dict["Sea Salt Icecream"] = self.options.seasaltpool.value
        elif self.options.goalchoice == goalChoice.option_Mission_Completed:
            self.item_quantity_dict["Sea Salt Icecream"] = 0

        #startingmission init
        self.starting_mission = self.random.randint(1, 91)
        name = getattr(ItemName, f"UnlockMission{self.starting_mission}")

        #character rando
        if self.options.charrando == charRando.option_Full_Character_Rando:
            for character, charData in Character_Table.items():
                if charData.khDaysID == self.options.startchar.value:
                    characterName = character
                    self.startChar = self.options.startchar.value
               
                
            self.multiworld.push_precollected(self.create_item(characterName))
            self.item_quantity_dict[characterName] -= 1
        #mission set rando
        else:
            self.missionSetRando = {}
            self.startChar = 0
            for char in Character_Table:
                self.item_quantity_dict[char] = 0
            for mission in range(1,92):
                character = self.random.choice(tuple(Character_Table))
                self.missionSetRando[mission] = Character_Table[character].khDaysID

        #starting scan(cuz gear alone in inventory crash game)
        self.scan = Abillity_Table["Scan"].khDaysID   
        self.multiworld.push_precollected(self.create_item("Scan"))
        self.item_quantity_dict["Scan"] -= 1

        #the mission precollect is here?????????
        self.multiworld.push_precollected(self.create_item(name))
        self.item_quantity_dict[name] -= 1
        

        #itempool generation(clean up looks a bit dirty)
        itempool = []
        
        for name, quantity in self.item_quantity_dict.items():
            for _ in range(quantity):
                itempool.append(self.create_item(name))
        unfilled_locations = self.multiworld.get_unfilled_locations(self.player)
        remaining_locations = len(unfilled_locations) - len(itempool)

        for _ in range(remaining_locations):
            itempool.append(self.create_filler())

        self.multiworld.itempool += itempool

    def get_filler_item_name(self):
        return self.random.choice(tuple(Consumable_Table))

    def create_regions(self):
        create_region(self)
        connect_regions(self)

    def set_rules(self):
        set_rules(self)


    #organize this, this shit is gonna GROWWWWWWWWWWWW
    def fill_slot_data(self):
        startSettings = {}
        startSettings["starting_mission"] = self.starting_mission
        startSettings["gear_bundles"] = self.gear_bundles
        startSettings["items"] = {
            str(self.item_name_to_id[name]): {
                "id": data.khDaysID,
                "mission": data.missionUnlock,
                "character": data.characterUnlock,
                "seaSalt" : data.seaSalt,
                "pack": data.pack
            }
            for name, data in V2Items.items()
        }

        startSettings["starting_character"] = self.startChar
        startSettings["Starting Inventory"] = self.scan

        if self.options.charrando == charRando.option_Per_Mission_Rando:
            startSettings["missionSetRando"] = self.missionSetRando

        startSettings["charrando"] = self.options.charrando.value

        startSettings["Goal Choice"] = self.options.goalchoice.value

        if self.options.goalchoice.value == goalChoice.option_SeaSalt_Icecream:
            startSettings["Sea Salt Required"] = self.options.seasaltrequired.value
        return startSettings
