import typing

from BaseClasses import Location,Item


class DaysLocation(Location):
    game: str = "KH Days"

class LocationData(typing.NamedTuple):
    locationID: int

class ItemData(typing.NamedTuple):
    quantity : int = 0
    khDaysID : int = 0
    missionUnlock : bool = False
    characterUnlock : bool = False
    seaSalt : bool = False
    pack : bool = False
