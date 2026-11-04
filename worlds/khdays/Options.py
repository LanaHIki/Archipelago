from dataclasses import dataclass
from Options import PerGameCommonOptions, Toggle, Choice,Range

class charRando(Choice):
    """True rando or set per mission"""
    display_name = "Character Randomization Mode"
    option_Full_Character_Rando = 0
    option_Per_Mission_Rando = 1
    default = 0

class goalChoice(Choice):
    "Wether you want mission amount completed or sea salt icecream"
    display_name = "Goal Choice"
    option_Mission_Completed = 0
    option_SeaSalt_Icecream = 1
    default = 1

class seasaltRequired(Range):
    "How many Sea Salt Icecreams are required to fight Xion"
    display_name = "Icecream Required"
    range_start = 1
    range_end = 40
    default = 15

class seasaltPool(Range):
    "How many Sea Salt Icecreams are in the pool"
    display_name = "Icecream pool"
    range_start = 1
    range_end = 40
    default = 20

class startingCharacter(Choice):
    "If true character rando, this determines the starting character"
    display_name = "Starting Character"
    option_Roxas = 0
    option_Axel = 1
    option_Xigbar = 2
    option_Saix = 3
    option_Xaldin = 4
    option_Sora = 5
    option_Demyx = 6
    option_Larxene = 7
    option_Lexaeus = 8
    option_Luxord = 9
    option_Marluxia = 10
    option_Riku = 11
    option_Vexen = 12
    option_Xemnas = 13
    option_Xion = 14
    option_Zexion = 15
    option_Mickey = 16
    option_Donald = 17
    option_Goofy = 18
    option_DWRoxas = 19
    default = 0
    
@dataclass
class DaysOpts(PerGameCommonOptions):
    charrando: charRando
    goalchoice : goalChoice
    seasaltrequired : seasaltRequired
    seasaltpool : seasaltPool
    startchar : startingCharacter
