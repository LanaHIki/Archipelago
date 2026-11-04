
from worlds.generic.Rules import set_rule
from .Items import MagPacks, Character_Table
from .Names import RegionName
from .Names import ItemName
from .Options import goalChoice, charRando
from .Names import LocationName
def set_rules(world):
    for mission in range(1, 92):
        name = getattr(RegionName, f"Mission{mission}")
        item = getattr(ItemName, f"UnlockMission{mission}")
        region = world.multiworld.get_region(name, world.player)

        set_rule(
            region.entrances[0],
            lambda state, item=item: state.has(item, world.player)
        )

    completed = [
        f"Completed Mission {mission}"
        for mission in range(1, 92)
    ]
    checks = RulesChests()
    checks.chestRuleCheck(world)
    bosses = RulesBosses()
    bosses.bossRuleCheck(world)
    missions = RulesMissions()
    if world.options.charrando == charRando.option_Per_Mission_Rando:
        missions.mission4Character = world.missionSetRando[4]
    missions.missionRuleCheck(world)
    goal = world.multiworld.get_region(RegionName.DefeatRiku, world.player)

    if world.options.goalchoice == goalChoice.option_Mission_Completed:
        set_rule(
            goal.entrances[0],
            lambda state: sum(
                state.has(name, world.player) for name in completed
            ) >= 64
        )

    if world.options.goalchoice == goalChoice.option_SeaSalt_Icecream:
        set_rule(
            goal.entrances[0],
            lambda state: state.has(ItemName.SeaSaltIceCream, world.player, world.options.seasaltrequired.value)
            )
    world.multiworld.completion_condition[world.player] = (
        lambda state: state.has("Victory", world.player)
    )


class RulesMissions:
    mission4Character = None

    def mission4Check(self, state, player):
        unlocked = state.has_any(Character_Table.keys() - {ItemName.UnlockCharacterRoxas}, player)
        if self.mission4Character is not None:
            unlocked = self.mission4Character != 0
        attackMagic = state.has_any(MagPacks.keys() - {"Cure bundle", "Cura bundle", "Curaga bundle"}, player)
        return unlocked or attackMagic

    def mission10Check(self, state, player):
        return state.has_any(("Cure bundle", "Cura bundle", "Curaga bundle"), player)

    def mission71Check(self, state, player):
        return state.has_any(("Cure bundle", "Cura bundle", "Curaga bundle"), player)

    def missionRuleCheck(self, world):
        mission = world.multiworld.get_location(LocationName.Mission4Clear, world.player)
        set_rule(mission, lambda state: self.mission4Check(state, world.player))
        mission = world.multiworld.get_location(LocationName.Mission4Clear2, world.player)
        set_rule(mission, lambda state: self.mission4Check(state, world.player))
        mission = world.multiworld.get_location(LocationName.Mission4Clear3, world.player)
        set_rule(mission, lambda state: self.mission4Check(state, world.player))

        mission = world.multiworld.get_location(LocationName.Mission10Clear, world.player)
        set_rule(mission, lambda state: self.mission10Check(state, world.player))
        mission = world.multiworld.get_location(LocationName.Mission10Clear2, world.player)
        set_rule(mission, lambda state: self.mission10Check(state, world.player))
        mission = world.multiworld.get_location(LocationName.Mission10Clear3, world.player)
        set_rule(mission, lambda state: self.mission10Check(state, world.player))

        mission = world.multiworld.get_location(LocationName.Mission71Clear, world.player)
        set_rule(mission, lambda state: self.mission71Check(state, world.player))
        mission = world.multiworld.get_location(LocationName.Mission71Clear2, world.player)
        set_rule(mission, lambda state: self.mission71Check(state, world.player))
        mission = world.multiworld.get_location(LocationName.Mission71Clear3, world.player)
        set_rule(mission, lambda state: self.mission71Check(state, world.player))


class RulesBosses:
    def antlionCheck(self, state, player):
        gears = state.has("Progressive Gear", player, 5)
        magic = state.has_any(MagPacks, player)
        return gears and magic

    def infernalEngineCheck(self, state, player):
        gears = state.has("Progressive Gear", player, 5)
        magic = state.has_any(MagPacks, player)
        return gears and magic

    def guardArmorCheck(self, state, player):
        gears = state.has("Progressive Gear", player, 5)
        magic = state.has_any(MagPacks, player)
        return gears and magic

    def leechgraveCheck(self, state, player):
        gears = state.has("Progressive Gear", player, 5)
        magic = state.has_any(MagPacks, player)
        return gears and magic

    def crimsonPranksterCheck(self, state, player):
        gears = state.has("Progressive Gear", player, 5)
        magic = state.has_any(MagPacks, player)
        return gears and magic

    def rulerOfTheSkyCheck(self, state, player):
        gears = state.has("Progressive Gear", player, 5)
        magic = state.has_any(MagPacks, player)
        return gears and magic

    def xionCheck(self, state, player):
        gears = state.has("Progressive Gear", player, 5)
        magic = state.has_any(MagPacks, player)
        return gears and magic

    def saixCheck(self, state, player):
        gears = state.has("Progressive Gear", player, 5)
        magic = state.has_any(MagPacks, player)
        return gears and magic

    def rikuCheck(self, state, player):
        gears = state.has("Progressive Gear", player, 5)
        magic = state.has_any(MagPacks, player)
        return gears and magic

    def bossRuleCheck(self, world):
        boss = world.multiworld.get_location(LocationName.Mission32Clear, world.player)
        set_rule(boss, lambda state: self.antlionCheck(state, world.player))

        boss = world.multiworld.get_location(LocationName.Mission32Clear2, world.player)
        set_rule(boss, lambda state: self.antlionCheck(state, world.player))

        boss = world.multiworld.get_location(LocationName.Mission32Clear3, world.player)
        set_rule(boss, lambda state: self.antlionCheck(state, world.player))

        boss = world.multiworld.get_location("Completed Mission 32", world.player)
        set_rule(boss, lambda state: self.antlionCheck(state, world.player))

        boss = world.multiworld.get_location(LocationName.Mission50Clear, world.player)
        set_rule(boss, lambda state: self.infernalEngineCheck(state, world.player))

        boss = world.multiworld.get_location(LocationName.Mission50Clear2, world.player)
        set_rule(boss, lambda state: self.infernalEngineCheck(state, world.player))

        boss = world.multiworld.get_location(LocationName.Mission50Clear3, world.player)
        set_rule(boss, lambda state: self.infernalEngineCheck(state, world.player))

        boss = world.multiworld.get_location("Completed Mission 50", world.player)
        set_rule(boss, lambda state: self.infernalEngineCheck(state, world.player))

        boss = world.multiworld.get_location(LocationName.Mission61Clear, world.player)
        set_rule(boss, lambda state: self.guardArmorCheck(state, world.player))

        boss = world.multiworld.get_location(LocationName.Mission61Clear2, world.player)
        set_rule(boss, lambda state: self.guardArmorCheck(state, world.player))

        boss = world.multiworld.get_location(LocationName.Mission61Clear3, world.player)
        set_rule(boss, lambda state: self.guardArmorCheck(state, world.player))

        boss = world.multiworld.get_location("Completed Mission 61", world.player)
        set_rule(boss, lambda state: self.guardArmorCheck(state, world.player))

        boss = world.multiworld.get_location(LocationName.Mission66Clear, world.player)
        set_rule(boss, lambda state: self.leechgraveCheck(state, world.player))

        boss = world.multiworld.get_location(LocationName.Mission66Clear2, world.player)
        set_rule(boss, lambda state: self.leechgraveCheck(state, world.player))

        boss = world.multiworld.get_location(LocationName.Mission66Clear3, world.player)
        set_rule(boss, lambda state: self.leechgraveCheck(state, world.player))

        boss = world.multiworld.get_location("Completed Mission 66", world.player)
        set_rule(boss, lambda state: self.leechgraveCheck(state, world.player))

        boss = world.multiworld.get_location(LocationName.Mission69Clear, world.player)
        set_rule(boss, lambda state: self.crimsonPranksterCheck(state, world.player))

        boss = world.multiworld.get_location(LocationName.Mission69Clear2, world.player)
        set_rule(boss, lambda state: self.crimsonPranksterCheck(state, world.player))

        boss = world.multiworld.get_location(LocationName.Mission69Clear3, world.player)
        set_rule(boss, lambda state: self.crimsonPranksterCheck(state, world.player))

        boss = world.multiworld.get_location("Completed Mission 69", world.player)
        set_rule(boss, lambda state: self.crimsonPranksterCheck(state, world.player))

        boss = world.multiworld.get_location(LocationName.Mission78Clear, world.player)
        set_rule(boss, lambda state: self.rulerOfTheSkyCheck(state, world.player))

        boss = world.multiworld.get_location(LocationName.Mission78Clear2, world.player)
        set_rule(boss, lambda state: self.rulerOfTheSkyCheck(state, world.player))

        boss = world.multiworld.get_location(LocationName.Mission78Clear3, world.player)
        set_rule(boss, lambda state: self.rulerOfTheSkyCheck(state, world.player))

        boss = world.multiworld.get_location("Completed Mission 78", world.player)
        set_rule(boss, lambda state: self.rulerOfTheSkyCheck(state, world.player))

        boss = world.multiworld.get_location(LocationName.Mission90Clear, world.player)
        set_rule(boss, lambda state: self.xionCheck(state, world.player))

        boss = world.multiworld.get_location(LocationName.Mission90Clear2, world.player)
        set_rule(boss, lambda state: self.xionCheck(state, world.player))

        boss = world.multiworld.get_location(LocationName.Mission90Clear3, world.player)
        set_rule(boss, lambda state: self.xionCheck(state, world.player))

        boss = world.multiworld.get_location("Completed Mission 90", world.player)
        set_rule(boss, lambda state: self.xionCheck(state, world.player))

        boss = world.multiworld.get_location(LocationName.Mission91Clear, world.player)
        set_rule(boss, lambda state: self.saixCheck(state, world.player))

        boss = world.multiworld.get_location(LocationName.Mission91Clear2, world.player)
        set_rule(boss, lambda state: self.saixCheck(state, world.player))

        boss = world.multiworld.get_location(LocationName.Mission91Clear3, world.player)
        set_rule(boss, lambda state: self.saixCheck(state, world.player))

        boss = world.multiworld.get_location("Completed Mission 91", world.player)
        set_rule(boss, lambda state: self.saixCheck(state, world.player))

        boss = world.multiworld.get_location("Defeat Riku", world.player)
        set_rule(boss, lambda state: self.rikuCheck(state, world.player))


class RulesChests:
    def argrabahRoofCheck(self, state,player):
        airslide = state.has("Progressive Air Slide",player)
        anyHiJump = state.has("Progressive High Jump",player)
        hijumpSlide = anyHiJump and airslide

        bigHiJump = state.has("Progressive High Jump",player,2)

        glide = state.has("Progressive Glide", player)

        return hijumpSlide or bigHiJump or glide


    def aliceHedgeCheck(self,state,player):
        return state.has("Progressive Glide", player) or state.has("Progressive High Jump", player, 2)



    def twilightRoofCheck(self,state,player):
        return state.has("Progressive Glide", player) or state.has("Progressive High Jump", player, 2)


    def caveHiChest(self,state,player):
        return state.has("Progressive High Jump",player,2)

    def secretDepthsChestCheck(self, state, player):
        return state.has("Progressive High Jump", player)

    def caveHiBackChest(self,state,player):
        hiJump = state.has("Progressive High Jump",player,2)
        glide = state.has("Progressive Glide", player)
        return hiJump and glide

    def chestRuleCheck(self,world):
        #mission 15, 16, 32, 82
        chest = world.multiworld.get_location(LocationName.Mission15Chest2, world.player)
        set_rule(chest, lambda state: self.argrabahRoofCheck(state,world.player))
    
        chest = world.multiworld.get_location(LocationName.Mission16Chest2, world.player)
        set_rule(chest, lambda state: self.argrabahRoofCheck(state,world.player))

        chest = world.multiworld.get_location(LocationName.Mission32Chest2, world.player)
        set_rule(chest, lambda state: self.argrabahRoofCheck(state,world.player))

        chest = world.multiworld.get_location(LocationName.Mission19Chest0, world.player)
        set_rule(chest, lambda state: self.argrabahRoofCheck(state,world.player))

        chest = world.multiworld.get_location(LocationName.Mission82Chest1, world.player)
        set_rule(chest, lambda state: self.argrabahRoofCheck(state,world.player))

        chest = world.multiworld.get_location(LocationName.Mission34Chest0, world.player)
        set_rule(chest, lambda state: self.argrabahRoofCheck(state,world.player))

        chest = world.multiworld.get_location(LocationName.Mission51Chest7, world.player)
        set_rule(chest, lambda state: self.aliceHedgeCheck(state,world.player))

        chest = world.multiworld.get_location(LocationName.Mission55Chest4, world.player)
        set_rule(chest, lambda state: self.aliceHedgeCheck(state,world.player))

        chest = world.multiworld.get_location(LocationName.Mission67Chest4, world.player)
        set_rule(chest, lambda state: self.aliceHedgeCheck(state,world.player))

        chest = world.multiworld.get_location(LocationName.Mission59Chest2, world.player)
        set_rule(chest, lambda state: self.twilightRoofCheck(state,world.player))

        chest = world.multiworld.get_location(LocationName.Mission48Chest7, world.player)
        set_rule(chest, lambda state: self.caveHiChest(state,world.player))

        chest = world.multiworld.get_location(LocationName.Mission48Chest5, world.player)
        set_rule(chest, lambda state: self.caveHiBackChest(state,world.player))

        chest = world.multiworld.get_location(LocationName.Mission68Chest3, world.player)
        set_rule(chest, lambda state: self.caveHiBackChest(state,world.player))

        chest = world.multiworld.get_location(LocationName.Mission90Chest2, world.player)
        set_rule(chest, lambda state: self.secretDepthsChestCheck(state,world.player))

    
