import typing

from BaseClasses import MultiWorld, Region, Item, ItemClassification
from . import Locations

from .Names import LocationName
from .SubClasses import DaysLocation
from .Names import RegionName

DAYSREGIONS: typing.Dict[str,typing.List[str]] = {
    "Menu" : [],
    RegionName.Mission1: [
        LocationName.Mission1Clear,
        LocationName.Mission1Clear2,
        LocationName.Mission1Clear3,
        LocationName.Mission1Chest0
    ],

    RegionName.Mission2: [
        LocationName.Mission2Clear,
        LocationName.Mission2Clear2,
        LocationName.Mission2Clear3
    ],

    RegionName.Mission3: [
        LocationName.Mission3Clear,
        LocationName.Mission3Clear2,
        LocationName.Mission3Clear3,
        LocationName.Mission3Chest0
    ],

    RegionName.Mission4: [
        LocationName.Mission4Clear,
        LocationName.Mission4Clear2,
        LocationName.Mission4Clear3,
        LocationName.Mission4Chest0,
        LocationName.Mission4Chest1,
        LocationName.Mission4Chest2
    ],

    RegionName.Mission5: [
        LocationName.Mission5Clear,
        LocationName.Mission5Clear2,
        LocationName.Mission5Clear3,
        LocationName.Mission5Chest0
    ],

    RegionName.Mission6: [
        LocationName.Mission6Clear,
        LocationName.Mission6Clear2,
        LocationName.Mission6Clear3
    ],

    RegionName.Mission7: [
        LocationName.Mission7Clear,
        LocationName.Mission7Clear2,
        LocationName.Mission7Clear3,
        LocationName.Mission7Chest0,
        LocationName.Mission7Chest1,
        LocationName.Mission7Chest2
    ],

    RegionName.Mission8: [
        LocationName.Mission8Clear,
        LocationName.Mission8Clear2,
        LocationName.Mission8Clear3,
        LocationName.Mission8Chest0,
        LocationName.Mission8Chest1
    ],

    RegionName.Mission9: [
        LocationName.Mission9Clear,
        LocationName.Mission9Clear2,
        LocationName.Mission9Clear3,
        LocationName.Mission9Chest0,
        LocationName.Mission9Chest1,
        LocationName.Mission9Chest2,
        LocationName.Mission9Chest3,
        LocationName.Mission9Chest4,
        LocationName.Mission9Chest5,
        LocationName.Mission9Chest6
    ],

    RegionName.Mission10: [
        LocationName.Mission10Clear,
        LocationName.Mission10Clear2,
        LocationName.Mission10Clear3
    ],

    RegionName.Mission11: [
        LocationName.Mission11Clear,
        LocationName.Mission11Clear2,
        LocationName.Mission11Clear3,
        LocationName.Mission11Chest0,
        LocationName.Mission11Chest1,
        LocationName.Mission11Chest2,
        LocationName.Mission11Chest3,
        LocationName.Mission11Chest4
    ],

    RegionName.Mission12: [
        LocationName.Mission12Clear,
        LocationName.Mission12Clear2,
        LocationName.Mission12Clear3,
        LocationName.Mission12Chest0,
        LocationName.Mission12Chest1
    ],

    RegionName.Mission13: [
        LocationName.Mission13Chest0,
        LocationName.Mission13Clear,
        LocationName.Mission13Clear2,
        LocationName.Mission13Clear3
    ],

    RegionName.Mission14: [
        LocationName.Mission14Clear,
        LocationName.Mission14Clear2,
        LocationName.Mission14Clear3,
        LocationName.Mission14Chest0,
        LocationName.Mission14Chest1,
        LocationName.Mission14Chest2,
        LocationName.Mission14Chest3,
        LocationName.Mission14Chest4
    ],

    RegionName.Mission15: [
        LocationName.Mission15Clear,
        LocationName.Mission15Clear2,
        LocationName.Mission15Clear3,
        LocationName.Mission15Chest0,
        LocationName.Mission15Chest1,
        LocationName.Mission15Chest2,
        LocationName.Mission15Chest3,
        LocationName.Mission15Chest4
    ],

    RegionName.Mission16: [
        LocationName.Mission16Clear,
        LocationName.Mission16Clear2,
        LocationName.Mission16Clear3,
        LocationName.Mission16Chest0,
        LocationName.Mission16Chest1,
        LocationName.Mission16Chest2,
        LocationName.Mission16Chest3,
        LocationName.Mission16Chest4
    ],

    RegionName.Mission17: [
        LocationName.Mission17Clear,
        LocationName.Mission17Clear2,
        LocationName.Mission17Clear3,
        LocationName.Mission17Chest0,
        LocationName.Mission17Chest1
    ],

    RegionName.Mission18: [
        LocationName.Mission18Clear,
        LocationName.Mission18Clear2,
        LocationName.Mission18Clear3,
        LocationName.Mission18Chest0,
        LocationName.Mission18Chest1,
        LocationName.Mission18Chest2,
        LocationName.Mission18Chest3
    ],

    RegionName.Mission19: [
        LocationName.Mission19Clear,
        LocationName.Mission19Clear2,
        LocationName.Mission19Clear3,
        LocationName.Mission19Chest0,
        LocationName.Mission19Chest1,
        LocationName.Mission19Chest2
    ],

    RegionName.Mission20: [
        LocationName.Mission20Clear,
        LocationName.Mission20Clear2,
        LocationName.Mission20Clear3,
        LocationName.Mission20Chest0,
        LocationName.Mission20Chest1
    ],

    RegionName.Mission21: [
        LocationName.Mission21Clear,
        LocationName.Mission21Clear2,
        LocationName.Mission21Clear3,
        LocationName.Mission21Chest0,
        LocationName.Mission21Chest1,
        LocationName.Mission21Chest2,
        LocationName.Mission21Chest3,
        LocationName.Mission21Chest4,
        LocationName.Mission21Chest5,
        LocationName.Mission21Chest6,
        LocationName.Mission21Chest7
    ],

    RegionName.Mission22: [
        LocationName.Mission22Clear,
        LocationName.Mission22Clear2,
        LocationName.Mission22Clear3,
        LocationName.Mission22Chest0,
        LocationName.Mission22Chest1,
        LocationName.Mission22Chest2,
        LocationName.Mission22Chest3,
        LocationName.Mission22Chest4
    ],

    RegionName.Mission23: [
        LocationName.Mission23Clear,
        LocationName.Mission23Clear2,
        LocationName.Mission23Clear3,
        LocationName.Mission23Chest0,
        LocationName.Mission23Chest1,
        LocationName.Mission23Chest2,
        LocationName.Mission23Chest3,
        LocationName.Mission23Chest4,
        LocationName.Mission23Chest5,
        LocationName.Mission23Chest6
    ],

    RegionName.Mission24: [
        LocationName.Mission24Clear,
        LocationName.Mission24Clear2,
        LocationName.Mission24Clear3,
        LocationName.Mission24Chest0,
        LocationName.Mission24Chest1,
        LocationName.Mission24Chest2,
        LocationName.Mission24Chest3,
        LocationName.Mission24Chest4,
        LocationName.Mission24Chest5,
        LocationName.Mission24Chest6,
        LocationName.Mission24Chest7
    ],

    RegionName.Mission25: [
        LocationName.Mission25Clear,
        LocationName.Mission25Clear2,
        LocationName.Mission25Clear3,
        LocationName.Mission25Chest0,
        LocationName.Mission25Chest1
    ],

    RegionName.Mission26: [
        LocationName.Mission26Clear,
        LocationName.Mission26Clear2,
        LocationName.Mission26Clear3,
        LocationName.Mission26Chest0,
        LocationName.Mission26Chest1,
        LocationName.Mission26Chest2,
        LocationName.Mission26Chest3,
        LocationName.Mission26Chest4,
        LocationName.Mission26Chest5
    ],

    RegionName.Mission27: [
        LocationName.Mission27Clear,
        LocationName.Mission27Clear2,
        LocationName.Mission27Clear3,
        LocationName.Mission27Chest0,
        LocationName.Mission27Chest1,
        LocationName.Mission27Chest2,
        LocationName.Mission27Chest3,
        LocationName.Mission27Chest4,
        LocationName.Mission27Chest5
    ],

    RegionName.Mission28: [
        LocationName.Mission28Clear,
        LocationName.Mission28Clear2,
        LocationName.Mission28Clear3,
        LocationName.Mission28Chest0,
        LocationName.Mission28Chest1,
        LocationName.Mission28Chest2,
        LocationName.Mission28Chest3,
        LocationName.Mission28Chest4,
        LocationName.Mission28Chest5
    ],

    RegionName.Mission29: [
        LocationName.Mission29Clear,
        LocationName.Mission29Clear2,
        LocationName.Mission29Clear3,
        LocationName.Mission29Chest0,
        LocationName.Mission29Chest1,
        LocationName.Mission29Chest2,
        LocationName.Mission29Chest3,
        LocationName.Mission29Chest4,
        LocationName.Mission29Chest5,
        LocationName.Mission29Chest6
    ],

    RegionName.Mission30: [
        LocationName.Mission30Clear,
        LocationName.Mission30Clear2,
        LocationName.Mission30Clear3,
        LocationName.Mission30Chest0,
        LocationName.Mission30Chest1,
        LocationName.Mission30Chest2,
        LocationName.Mission30Chest3,
        LocationName.Mission30Chest4,
        LocationName.Mission30Chest5
    ],

    RegionName.Mission31: [
        LocationName.Mission31Clear,
        LocationName.Mission31Clear2,
        LocationName.Mission31Clear3,
        LocationName.Mission31Chest0,
        LocationName.Mission31Chest1,
        LocationName.Mission31Chest2,
        LocationName.Mission31Chest3,
        LocationName.Mission31Chest4,
        LocationName.Mission31Chest5,
        LocationName.Mission31Chest6
    ],

    RegionName.Mission32: [
        LocationName.Mission32Clear,
        LocationName.Mission32Clear2,
        LocationName.Mission32Clear3,
        LocationName.Mission32Chest0,
        LocationName.Mission32Chest1,
        LocationName.Mission32Chest2,
        LocationName.Mission32Chest3,
        LocationName.Mission32Chest4,
        LocationName.Mission32Chest5,
        LocationName.Mission32Chest6,
        LocationName.Mission32Chest7
    ],

    RegionName.Mission33: [
        LocationName.Mission33Clear,
        LocationName.Mission33Clear2,
        LocationName.Mission33Clear3
    ],

    RegionName.Mission34: [
        LocationName.Mission34Clear,
        LocationName.Mission34Clear2,
        LocationName.Mission34Clear3,
        LocationName.Mission34Chest0,
        LocationName.Mission34Chest1,
        LocationName.Mission34Chest2,
        LocationName.Mission34Chest3,
        LocationName.Mission34Chest4,
        LocationName.Mission34Chest5,
        LocationName.Mission34Chest6,
        LocationName.Mission34Chest7
    ],

    RegionName.Mission35: [
        LocationName.Mission35Clear,
        LocationName.Mission35Clear2,
        LocationName.Mission35Clear3,
        LocationName.Mission35Chest0,
        LocationName.Mission35Chest1,
        LocationName.Mission35Chest2,
        LocationName.Mission35Chest3,
        LocationName.Mission35Chest4,
        LocationName.Mission35Chest5
    ],

    RegionName.Mission36: [
        LocationName.Mission36Clear,
        LocationName.Mission36Clear2,
        LocationName.Mission36Clear3,
        LocationName.Mission36Chest0,
        LocationName.Mission36Chest1
    ],

    RegionName.Mission37: [
        LocationName.Mission37Clear,
        LocationName.Mission37Clear2,
        LocationName.Mission37Clear3
    ],

    RegionName.Mission38: [
        LocationName.Mission38Clear,
        LocationName.Mission38Clear2,
        LocationName.Mission38Clear3,
        LocationName.Mission38Chest0,
        LocationName.Mission38Chest1,
        LocationName.Mission38Chest2,
        LocationName.Mission38Chest3,
        LocationName.Mission38Chest4,
        LocationName.Mission38Chest5
    ],

    RegionName.Mission39: [
        LocationName.Mission39Clear,
        LocationName.Mission39Clear2,
        LocationName.Mission39Clear3,
        LocationName.Mission39Chest0,
        LocationName.Mission39Chest1,
        LocationName.Mission39Chest2
    ],

    RegionName.Mission40: [
        LocationName.Mission40Clear,
        LocationName.Mission40Clear2,
        LocationName.Mission40Clear3,
        LocationName.Mission40Chest0,
        LocationName.Mission40Chest1,
        LocationName.Mission40Chest2
    ],

    RegionName.Mission41: [
        LocationName.Mission41Clear,
        LocationName.Mission41Clear2,
        LocationName.Mission41Clear3,
        LocationName.Mission41Chest0,
        LocationName.Mission41Chest1,
        LocationName.Mission41Chest2
    ],

    RegionName.Mission42: [
        LocationName.Mission42Clear,
        LocationName.Mission42Clear2,
        LocationName.Mission42Clear3,
        LocationName.Mission42Chest0,
        LocationName.Mission42Chest1,
        LocationName.Mission42Chest2
    ],

    RegionName.Mission43: [
        LocationName.Mission43Clear,
        LocationName.Mission43Clear2,
        LocationName.Mission43Clear3,
        LocationName.Mission43Chest0,
        LocationName.Mission43Chest1,
        LocationName.Mission43Chest2,
        LocationName.Mission43Chest3
    ],

    RegionName.Mission44: [
        LocationName.Mission44Clear,
        LocationName.Mission44Clear2,
        LocationName.Mission44Clear3,
        LocationName.Mission44Chest0,
        LocationName.Mission44Chest1
    ],

    RegionName.Mission45: [
        LocationName.Mission45Clear,
        LocationName.Mission45Clear2,
        LocationName.Mission45Clear3,
        LocationName.Mission45Chest0,
        LocationName.Mission45Chest1,
        LocationName.Mission45Chest2,
        LocationName.Mission45Chest3
    ],

    RegionName.Mission46: [
        LocationName.Mission46Clear,
        LocationName.Mission46Clear2,
        LocationName.Mission46Clear3,
        LocationName.Mission46Chest0,
        LocationName.Mission46Chest1,
        LocationName.Mission46Chest2
    ],

    RegionName.Mission47: [
        LocationName.Mission47Clear,
        LocationName.Mission47Clear2,
        LocationName.Mission47Clear3,
        LocationName.Mission47Chest0,
        LocationName.Mission47Chest1,
        LocationName.Mission47Chest2
    ],

    RegionName.Mission48: [
        LocationName.Mission48Clear,
        LocationName.Mission48Clear2,
        LocationName.Mission48Clear3,
        LocationName.Mission48Chest0,
        LocationName.Mission48Chest1,
        LocationName.Mission48Chest2,
        LocationName.Mission48Chest3,
        LocationName.Mission48Chest4,
        LocationName.Mission48Chest5,
        LocationName.Mission48Chest6,
        LocationName.Mission48Chest7
    ],

    RegionName.Mission49: [
        LocationName.Mission49Clear,
        LocationName.Mission49Clear2,
        LocationName.Mission49Clear3,
        LocationName.Mission49Chest0,
        LocationName.Mission49Chest1,
        LocationName.Mission49Chest2,
        LocationName.Mission49Chest3,
        LocationName.Mission49Chest4,
        LocationName.Mission49Chest5,
        LocationName.Mission49Chest6,
        LocationName.Mission49Chest7
    ],

    RegionName.Mission50: [
        LocationName.Mission50Clear,
        LocationName.Mission50Clear2,
        LocationName.Mission50Clear3,
        LocationName.Mission50Chest0,
        LocationName.Mission50Chest1,
        LocationName.Mission50Chest2,
        LocationName.Mission50Chest3
    ],

    RegionName.Mission51: [
        LocationName.Mission51Clear,
        LocationName.Mission51Clear2,
        LocationName.Mission51Clear3,
        LocationName.Mission51Chest0,
        LocationName.Mission51Chest1,
        LocationName.Mission51Chest2,
        LocationName.Mission51Chest3,
        LocationName.Mission51Chest4,
        LocationName.Mission51Chest5,
        LocationName.Mission51Chest6,
        LocationName.Mission51Chest7
    ],

    RegionName.Mission52: [
        LocationName.Mission52Chest7,
        LocationName.Mission52Clear,
        LocationName.Mission52Clear2,
        LocationName.Mission52Clear3,
        LocationName.Mission52Chest0,
        LocationName.Mission52Chest1,
        LocationName.Mission52Chest2,
        LocationName.Mission52Chest3,
        LocationName.Mission52Chest4,
        LocationName.Mission52Chest5,
        LocationName.Mission52Chest6
    ],

    RegionName.Mission53: [
        LocationName.Mission53Clear,
        LocationName.Mission53Clear2,
        LocationName.Mission53Clear3
    ],

    RegionName.Mission54: [
        LocationName.Mission54Clear,
        LocationName.Mission54Clear2,
        LocationName.Mission54Clear3,
        LocationName.Mission54Chest0,
        LocationName.Mission54Chest1
    ],

    RegionName.Mission55: [
        LocationName.Mission55Clear,
        LocationName.Mission55Clear2,
        LocationName.Mission55Clear3,
        LocationName.Mission55Chest0,
        LocationName.Mission55Chest1,
        LocationName.Mission55Chest2,
        LocationName.Mission55Chest3,
        LocationName.Mission55Chest4
    ],

    RegionName.Mission56: [
        LocationName.Mission56Clear,
        LocationName.Mission56Clear2,
        LocationName.Mission56Clear3,
        LocationName.Mission56Chest0,
        LocationName.Mission56Chest1,
        LocationName.Mission56Chest2,
        LocationName.Mission56Chest3
    ],

    RegionName.Mission57: [
        LocationName.Mission57Clear,
        LocationName.Mission57Clear2,
        LocationName.Mission57Clear3,
        LocationName.Mission57Chest0,
        LocationName.Mission57Chest1,
        LocationName.Mission57Chest2,
        LocationName.Mission57Chest3,
        LocationName.Mission57Chest4,
        LocationName.Mission57Chest5,
        LocationName.Mission57Chest6
    ],

    RegionName.Mission58: [
        LocationName.Mission58Clear,
        LocationName.Mission58Clear2,
        LocationName.Mission58Clear3
    ],

    RegionName.Mission59: [
        LocationName.Mission59Clear,
        LocationName.Mission59Clear2,
        LocationName.Mission59Clear3,
        LocationName.Mission59Chest0,
        LocationName.Mission59Chest1,
        LocationName.Mission59Chest2
    ],

    RegionName.Mission60: [
        LocationName.Mission60Clear,
        LocationName.Mission60Clear2,
        LocationName.Mission60Clear3,
        LocationName.Mission60Chest0,
        LocationName.Mission60Chest1
    ],

    RegionName.Mission61: [
        LocationName.Mission61Clear,
        LocationName.Mission61Clear2,
        LocationName.Mission61Clear3,
        LocationName.Mission61Chest0,
        LocationName.Mission61Chest1,
        LocationName.Mission61Chest2
    ],

    RegionName.Mission62: [
        LocationName.Mission62Clear,
        LocationName.Mission62Clear2,
        LocationName.Mission62Clear3,
        LocationName.Mission62Chest0,
        LocationName.Mission62Chest1,
        LocationName.Mission62Chest2,
        LocationName.Mission62Chest3,
        LocationName.Mission62Chest4,
        LocationName.Mission62Chest5,
        LocationName.Mission62Chest6,
        LocationName.Mission62Chest7
    ],

    RegionName.Mission63: [
        LocationName.Mission63Clear,
        LocationName.Mission63Clear2,
        LocationName.Mission63Clear3,
        LocationName.Mission63Chest0,
        LocationName.Mission63Chest1,
        LocationName.Mission63Chest2,
        LocationName.Mission63Chest3,
        LocationName.Mission63Chest4,
        LocationName.Mission63Chest5,
        LocationName.Mission63Chest6
    ],

    RegionName.Mission64: [
        LocationName.Mission64Clear,
        LocationName.Mission64Clear2,
        LocationName.Mission64Clear3,
        LocationName.Mission64Chest0,
        LocationName.Mission64Chest1
    ],

    RegionName.Mission65: [
        LocationName.Mission65Clear,
        LocationName.Mission65Clear2,
        LocationName.Mission65Clear3,
        LocationName.Mission65Chest0,
        LocationName.Mission65Chest1,
        LocationName.Mission65Chest2,
        LocationName.Mission65Chest3,
        LocationName.Mission65Chest4,
        LocationName.Mission65Chest5,
        LocationName.Mission65Chest6,
        LocationName.Mission65Chest7
    ],

    RegionName.Mission66: [
        LocationName.Mission66Clear,
        LocationName.Mission66Clear2,
        LocationName.Mission66Clear3,
        LocationName.Mission66Chest0,
        LocationName.Mission66Chest1,
        LocationName.Mission66Chest2,
        LocationName.Mission66Chest3,
        LocationName.Mission66Chest4,
        LocationName.Mission66Chest5,
        LocationName.Mission66Chest6,
        LocationName.Mission66Chest7
    ],

    RegionName.Mission67: [
        LocationName.Mission67Clear,
        LocationName.Mission67Clear2,
        LocationName.Mission67Clear3,
        LocationName.Mission67Chest0,
        LocationName.Mission67Chest1,
        LocationName.Mission67Chest2,
        LocationName.Mission67Chest3,
        LocationName.Mission67Chest4,
        LocationName.Mission67Chest5,
        LocationName.Mission67Chest6
    ],

    RegionName.Mission68: [
        LocationName.Mission68Clear,
        LocationName.Mission68Clear2,
        LocationName.Mission68Clear3,
        LocationName.Mission68Chest0,
        LocationName.Mission68Chest1,
        LocationName.Mission68Chest2,
        LocationName.Mission68Chest3,
        LocationName.Mission68Chest4,
        LocationName.Mission68Chest5,
        LocationName.Mission68Chest6,
        LocationName.Mission68Chest7
    ],

    RegionName.Mission69: [
        LocationName.Mission69Clear,
        LocationName.Mission69Clear2,
        LocationName.Mission69Clear3,
        LocationName.Mission69Chest0,
        LocationName.Mission69Chest1,
        LocationName.Mission69Chest2
    ],

    RegionName.Mission70: [
        LocationName.Mission70Clear,
        LocationName.Mission70Clear2,
        LocationName.Mission70Clear3,
        LocationName.Mission70Chest0
    ],

    RegionName.Mission71: [
        LocationName.Mission71Clear,
        LocationName.Mission71Clear2,
        LocationName.Mission71Clear3
    ],

    RegionName.Mission72: [
        LocationName.Mission72Clear,
        LocationName.Mission72Clear2,
        LocationName.Mission72Clear3,
        LocationName.Mission72Chest0
    ],

    RegionName.Mission73: [
        LocationName.Mission73Clear,
        LocationName.Mission73Clear2,
        LocationName.Mission73Clear3,
        LocationName.Mission73Chest0,
        LocationName.Mission73Chest1
    ],

    RegionName.Mission74: [
        LocationName.Mission74Clear,
        LocationName.Mission74Clear2,
        LocationName.Mission74Clear3,
        LocationName.Mission74Chest0,
        LocationName.Mission74Chest1,
        LocationName.Mission74Chest2
    ],

    RegionName.Mission75: [
        LocationName.Mission75Clear,
        LocationName.Mission75Clear2,
        LocationName.Mission75Clear3,
        LocationName.Mission75Chest0,
        LocationName.Mission75Chest1,
        LocationName.Mission75Chest2
    ],

    RegionName.Mission76: [
        LocationName.Mission76Clear,
        LocationName.Mission76Clear2,
        LocationName.Mission76Clear3,
        LocationName.Mission76Chest0,
        LocationName.Mission76Chest1
    ],

    RegionName.Mission77: [
        LocationName.Mission77Clear,
        LocationName.Mission77Clear2,
        LocationName.Mission77Clear3
    ],

    RegionName.Mission78: [
        LocationName.Mission78Clear,
        LocationName.Mission78Clear2,
        LocationName.Mission78Clear3
    ],

    RegionName.Mission79: [
        LocationName.Mission79Clear,
        LocationName.Mission79Clear2,
        LocationName.Mission79Clear3,
        LocationName.Mission79Chest0,
        LocationName.Mission79Chest1,
        LocationName.Mission79Chest2,
        LocationName.Mission79Chest3
    ],

    RegionName.Mission80: [
        LocationName.Mission80Clear,
        LocationName.Mission80Clear2,
        LocationName.Mission80Clear3
    ],

    RegionName.Mission81: [
        LocationName.Mission81Clear,
        LocationName.Mission81Clear2,
        LocationName.Mission81Clear3,
        LocationName.Mission81Chest0,
        LocationName.Mission81Chest1,
        LocationName.Mission81Chest2,
        LocationName.Mission81Chest3,
        LocationName.Mission81Chest4,
        LocationName.Mission81Chest5
    ],

    RegionName.Mission82: [
        LocationName.Mission82Clear,
        LocationName.Mission82Clear2,
        LocationName.Mission82Clear3,
        LocationName.Mission82Chest0,
        LocationName.Mission82Chest1,
        LocationName.Mission82Chest2,
        LocationName.Mission82Chest3,
        LocationName.Mission82Chest4,
        LocationName.Mission82Chest5,
        LocationName.Mission82Chest6,
        LocationName.Mission82Chest7
    ],

    RegionName.Mission83: [
        LocationName.Mission83Clear,
        LocationName.Mission83Clear2,
        LocationName.Mission83Clear3,
        LocationName.Mission83Chest0,
        LocationName.Mission83Chest1,
        LocationName.Mission83Chest2,
        LocationName.Mission83Chest3,
        LocationName.Mission83Chest4,
        LocationName.Mission83Chest5,
        LocationName.Mission83Chest6,
        LocationName.Mission83Chest7
    ],

    RegionName.Mission84: [
        LocationName.Mission84Clear,
        LocationName.Mission84Clear2,
        LocationName.Mission84Clear3,
        LocationName.Mission84Chest0
    ],

    RegionName.Mission85: [
        LocationName.Mission85Clear,
        LocationName.Mission85Clear2,
        LocationName.Mission85Clear3,
        LocationName.Mission85Chest0,
        LocationName.Mission85Chest1,
        LocationName.Mission85Chest2,
        LocationName.Mission85Chest3
    ],

    RegionName.Mission86: [
        LocationName.Mission86Clear,
        LocationName.Mission86Clear2,
        LocationName.Mission86Clear3,
        LocationName.Mission86Chest0
    ],

    RegionName.Mission87: [
        LocationName.Mission87Clear,
        LocationName.Mission87Clear2,
        LocationName.Mission87Clear3,
        LocationName.Mission87Chest0,
        LocationName.Mission87Chest1,
        LocationName.Mission87Chest2,
        LocationName.Mission87Chest3,
        LocationName.Mission87Chest4
    ],

    RegionName.Mission88: [
        LocationName.Mission88Clear,
        LocationName.Mission88Clear2,
        LocationName.Mission88Clear3,
        LocationName.Mission88Chest0
    ],

    RegionName.Mission89: [
        LocationName.Mission89Clear,
        LocationName.Mission89Clear2,
        LocationName.Mission89Clear3,
        LocationName.Mission89Chest0,
        LocationName.Mission89Chest1,
        LocationName.Mission89Chest2,
        LocationName.Mission89Chest3,
        LocationName.Mission89Chest4,
        LocationName.Mission89Chest5,
        LocationName.Mission89Chest6,
        LocationName.Mission89Chest7
    ],

    RegionName.Mission90: [
        LocationName.Mission90Clear,
        LocationName.Mission90Clear2,
        LocationName.Mission90Clear3,
        LocationName.Mission90Chest0,
        LocationName.Mission90Chest1,
        LocationName.Mission90Chest2,
        LocationName.Mission90Chest3,
        LocationName.Mission90Chest4
    ],

    RegionName.Mission91: [
        LocationName.Mission91Clear,
        LocationName.Mission91Clear2,
        LocationName.Mission91Clear3,
        LocationName.Mission91Chest0,
        LocationName.Mission91Chest1
    ],

    RegionName.DefeatRiku: [],

}

def create_region(world):
    for name,locations in DAYSREGIONS.items():
        region = Region(name, world.player, world.multiworld)

        for locationName in locations:
            locationID = world.location_name_to_id[locationName]
            location = DaysLocation(world.player, locationName, locationID, region)
            region.locations.append(location)
        world.multiworld.regions.append(region)
        
        
    for mission in range(1, 92):
        name = getattr(RegionName, f"Mission{mission}")
        region = world.multiworld.get_region(name, world.player)
        name = f"Completed Mission {mission}"

        event = DaysLocation(world.player, name, None, region)
        event.place_locked_item(
            Item(name, ItemClassification.progression, None, world.player)
        )
        region.locations.append(event)

    region = world.multiworld.get_region(RegionName.DefeatRiku, world.player)
    event = DaysLocation(world.player, "Defeat Riku", None, region)
    event.place_locked_item(
        Item("Victory", ItemClassification.progression, None, world.player)
    )
    region.locations.append(event)


def connect_regions(world):
    menu = world.multiworld.get_region("Menu",world.player)

    for name in DAYSREGIONS:
        if name != "Menu":
            region = world.multiworld.get_region(name,world.player)
            menu.connect(region)
            
