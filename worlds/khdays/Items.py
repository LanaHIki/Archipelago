from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item
from .Names import ItemName
from .SubClasses import ItemData

Gear_Table = {
    ItemName.SkillGear: ItemData(1, 0x00C0),
    ItemName.SkillGearPlus: ItemData(1, 0x00C1),
    ItemName.LoadedGear: ItemData(1, 0x00C2),
    ItemName.LoadedGearPlus: ItemData(1, 0x00C3),
    ItemName.ValorGear: ItemData(1, 0x00C4),
    ItemName.ValorGearPlus: ItemData(1, 0x00C5),
    ItemName.CasualGear: ItemData(1, 0x00C6),
    ItemName.TechnicalGear: ItemData(1, 0x00C7),
    ItemName.TechnicalGearPlus: ItemData(1, 0x00C8),
    ItemName.ChronoGear: ItemData(1, 0x00C9),
    ItemName.ChronoGearPlus: ItemData(1, 0x00CA),
    ItemName.FearlessGear: ItemData(1, 0x00CB),
    ItemName.FearlessGearPlus: ItemData(1, 0x00CC),
    ItemName.LiftGear: ItemData(1, 0x00CD),
    ItemName.LiftGearPlus: ItemData(1, 0x00CE),
    ItemName.WildGear: ItemData(1, 0x00CF),
    ItemName.WildGearPlus: ItemData(1, 0x00D0),
    ItemName.MysteryGear: ItemData(1, 0x00D1),
    ItemName.DuelGearPlus: ItemData(1, 0x00D2),
    ItemName.DuelGear: ItemData(1, 0x00D3),
    ItemName.PhantomGear: ItemData(1, 0x00D4),
    ItemName.PhantomGearPlus: ItemData(1, 0x00D5),
    ItemName.PrestigeGearPlus: ItemData(1, 0x00D6),
    ItemName.PrestigeGear: ItemData(1, 0x00D7),
    ItemName.NimbleGearPlus: ItemData(1, 0x00D8),
    ItemName.NimbleGear: ItemData(1, 0x00D9),
    ItemName.OminGearP: ItemData(1, 0x00DA),
    ItemName.OminGear: ItemData(1, 0x00DB),
    ItemName.DuelGearPlus2: ItemData(1, 0x00DC),
    ItemName.PhantomGearPlus2: ItemData(1, 0x00DD),
    ItemName.HazardGear: ItemData(1, 0x00DE),
    ItemName.HazardGearPlus: ItemData(1, 0x00DF),
    ItemName.CrisisGear: ItemData(1, 0x00E0),
    ItemName.CrisisGearPlus: ItemData(1, 0x00E1),
    ItemName.ChampionGear: ItemData(1, 0x00E2),
    ItemName.ChampionGearPlus: ItemData(1, 0x00E3),
    ItemName.RageGearPlus: ItemData(1, 0x00E4),
    ItemName.RageGear: ItemData(1, 0x00E5),
    ItemName.ZeroGear: ItemData(1, 0x00E6),
    ItemName.PandorasGearPlus: ItemData(1, 0x00E7),
    ItemName.PandorasGear: ItemData(1, 0x00E8),
    ItemName.OmegaGearPlus: ItemData(1, 0x00E9),
    ItemName.OmegaGear: ItemData(1, 0x00EA),
    ItemName.UltimateGearPlus: ItemData(1, 0x00EB),
    ItemName.UltimateGear: ItemData(1, 0x00EC),
}

Mission_Table = {
    ItemName.UnlockMission1: ItemData(1, 1, missionUnlock=True),
    ItemName.UnlockMission2: ItemData(1, 2, missionUnlock=True),
    ItemName.UnlockMission3: ItemData(1, 3, missionUnlock=True),
    ItemName.UnlockMission4: ItemData(1, 4, missionUnlock=True),
    ItemName.UnlockMission5: ItemData(1, 5, missionUnlock=True),
    ItemName.UnlockMission6: ItemData(1, 6, missionUnlock=True),
    ItemName.UnlockMission7: ItemData(1, 7, missionUnlock=True),
    ItemName.UnlockMission8: ItemData(1, 8, missionUnlock=True),
    ItemName.UnlockMission9: ItemData(1, 9, missionUnlock=True),
    ItemName.UnlockMission10: ItemData(1, 10, missionUnlock=True),
    ItemName.UnlockMission11: ItemData(1, 11, missionUnlock=True),
    ItemName.UnlockMission12: ItemData(1, 12, missionUnlock=True),
    ItemName.UnlockMission13: ItemData(1, 13, missionUnlock=True),
    ItemName.UnlockMission14: ItemData(1, 14, missionUnlock=True),
    ItemName.UnlockMission15: ItemData(1, 15, missionUnlock=True),
    ItemName.UnlockMission16: ItemData(1, 16, missionUnlock=True),
    ItemName.UnlockMission17: ItemData(1, 17, missionUnlock=True),
    ItemName.UnlockMission18: ItemData(1, 18, missionUnlock=True),
    ItemName.UnlockMission19: ItemData(1, 19, missionUnlock=True),
    ItemName.UnlockMission20: ItemData(1, 20, missionUnlock=True),
    ItemName.UnlockMission21: ItemData(1, 21, missionUnlock=True),
    ItemName.UnlockMission22: ItemData(1, 22, missionUnlock=True),
    ItemName.UnlockMission23: ItemData(1, 23, missionUnlock=True),
    ItemName.UnlockMission24: ItemData(1, 24, missionUnlock=True),
    ItemName.UnlockMission25: ItemData(1, 25, missionUnlock=True),
    ItemName.UnlockMission26: ItemData(1, 26, missionUnlock=True),
    ItemName.UnlockMission27: ItemData(1, 27, missionUnlock=True),
    ItemName.UnlockMission28: ItemData(1, 28, missionUnlock=True),
    ItemName.UnlockMission29: ItemData(1, 29, missionUnlock=True),
    ItemName.UnlockMission30: ItemData(1, 30, missionUnlock=True),
    ItemName.UnlockMission31: ItemData(1, 31, missionUnlock=True),
    ItemName.UnlockMission32: ItemData(1, 32, missionUnlock=True),
    ItemName.UnlockMission33: ItemData(1, 33, missionUnlock=True),
    ItemName.UnlockMission34: ItemData(1, 34, missionUnlock=True),
    ItemName.UnlockMission35: ItemData(1, 35, missionUnlock=True),
    ItemName.UnlockMission36: ItemData(1, 36, missionUnlock=True),
    ItemName.UnlockMission37: ItemData(1, 37, missionUnlock=True),
    ItemName.UnlockMission38: ItemData(1, 38, missionUnlock=True),
    ItemName.UnlockMission39: ItemData(1, 39, missionUnlock=True),
    ItemName.UnlockMission40: ItemData(1, 40, missionUnlock=True),
    ItemName.UnlockMission41: ItemData(1, 41, missionUnlock=True),
    ItemName.UnlockMission42: ItemData(1, 42, missionUnlock=True),
    ItemName.UnlockMission43: ItemData(1, 43, missionUnlock=True),
    ItemName.UnlockMission44: ItemData(1, 44, missionUnlock=True),
    ItemName.UnlockMission45: ItemData(1, 45, missionUnlock=True),
    ItemName.UnlockMission46: ItemData(1, 46, missionUnlock=True),
    ItemName.UnlockMission47: ItemData(1, 47, missionUnlock=True),
    ItemName.UnlockMission48: ItemData(1, 48, missionUnlock=True),
    ItemName.UnlockMission49: ItemData(1, 49, missionUnlock=True),
    ItemName.UnlockMission50: ItemData(1, 50, missionUnlock=True),
    ItemName.UnlockMission51: ItemData(1, 51, missionUnlock=True),
    ItemName.UnlockMission52: ItemData(1, 52, missionUnlock=True),
    ItemName.UnlockMission53: ItemData(1, 53, missionUnlock=True),
    ItemName.UnlockMission54: ItemData(1, 54, missionUnlock=True),
    ItemName.UnlockMission55: ItemData(1, 55, missionUnlock=True),
    ItemName.UnlockMission56: ItemData(1, 56, missionUnlock=True),
    ItemName.UnlockMission57: ItemData(1, 57, missionUnlock=True),
    ItemName.UnlockMission58: ItemData(1, 58, missionUnlock=True),
    ItemName.UnlockMission59: ItemData(1, 59, missionUnlock=True),
    ItemName.UnlockMission60: ItemData(1, 60, missionUnlock=True),
    ItemName.UnlockMission61: ItemData(1, 61, missionUnlock=True),
    ItemName.UnlockMission62: ItemData(1, 62, missionUnlock=True),
    ItemName.UnlockMission63: ItemData(1, 63, missionUnlock=True),
    ItemName.UnlockMission64: ItemData(1, 64, missionUnlock=True),
    ItemName.UnlockMission65: ItemData(1, 65, missionUnlock=True),
    ItemName.UnlockMission66: ItemData(1, 66, missionUnlock=True),
    ItemName.UnlockMission67: ItemData(1, 67, missionUnlock=True),
    ItemName.UnlockMission68: ItemData(1, 68, missionUnlock=True),
    ItemName.UnlockMission69: ItemData(1, 69, missionUnlock=True),
    ItemName.UnlockMission70: ItemData(1, 70, missionUnlock=True),
    ItemName.UnlockMission71: ItemData(1, 71, missionUnlock=True),
    ItemName.UnlockMission72: ItemData(1, 72, missionUnlock=True),
    ItemName.UnlockMission73: ItemData(1, 73, missionUnlock=True),
    ItemName.UnlockMission74: ItemData(1, 74, missionUnlock=True),
    ItemName.UnlockMission75: ItemData(1, 75, missionUnlock=True),
    ItemName.UnlockMission76: ItemData(1, 76, missionUnlock=True),
    ItemName.UnlockMission77: ItemData(1, 77, missionUnlock=True),
    ItemName.UnlockMission78: ItemData(1, 78, missionUnlock=True),
    ItemName.UnlockMission79: ItemData(1, 79, missionUnlock=True),
    ItemName.UnlockMission80: ItemData(1, 80, missionUnlock=True),
    ItemName.UnlockMission81: ItemData(1, 81, missionUnlock=True),
    ItemName.UnlockMission82: ItemData(1, 82, missionUnlock=True),
    ItemName.UnlockMission83: ItemData(1, 83, missionUnlock=True),
    ItemName.UnlockMission84: ItemData(1, 84, missionUnlock=True),
    ItemName.UnlockMission85: ItemData(1, 85, missionUnlock=True),
    ItemName.UnlockMission86: ItemData(1, 86, missionUnlock=True),
    ItemName.UnlockMission87: ItemData(1, 87, missionUnlock=True),
    ItemName.UnlockMission88: ItemData(1, 88, missionUnlock=True),
    ItemName.UnlockMission89: ItemData(1, 89, missionUnlock=True),
    ItemName.UnlockMission90: ItemData(1, 90, missionUnlock=True),
    ItemName.UnlockMission91: ItemData(1, 91, missionUnlock=True),
}

Character_Table = {
    ItemName.UnlockCharacterRoxas: ItemData(1, 0, characterUnlock=True),
    ItemName.UnlockCharacterAxel: ItemData(1, 1, characterUnlock=True),
    ItemName.UnlockCharacterXion: ItemData(1, 14, characterUnlock=True),
    ItemName.UnlockCharacterSaix: ItemData(1, 3, characterUnlock=True),
    ItemName.UnlockCharacterXaldin: ItemData(1, 4, characterUnlock=True),
    ItemName.UnlockCharacterSora: ItemData(1, 5, characterUnlock=True),
    ItemName.UnlockCharacterDemyx: ItemData(1, 6, characterUnlock=True),
    ItemName.UnlockCharacterLarxene: ItemData(1, 7, characterUnlock=True),
    ItemName.UnlockCharacterLexaeus: ItemData(1, 8, characterUnlock=True),
    ItemName.UnlockCharacterLuxord: ItemData(1, 9, characterUnlock=True),
    ItemName.UnlockCharacterMarluxia: ItemData(1, 10, characterUnlock=True),
    ItemName.UnlockCharacterRiku: ItemData(1, 11, characterUnlock=True),
    ItemName.UnlockCharacterVexen: ItemData(1, 12, characterUnlock=True),
    ItemName.UnlockCharacterXemnas: ItemData(1, 13, characterUnlock=True),
    ItemName.UnlockCharacterXigbar: ItemData(1, 2, characterUnlock=True),
    ItemName.UnlockCharacterZexion: ItemData(1, 15, characterUnlock=True),
    ItemName.UnlockCharacterMickey: ItemData(1, 16, characterUnlock=True),
    ItemName.UnlockCharacterGoofy: ItemData(1, 18, characterUnlock=True),
    ItemName.UnlockCharacterDonald: ItemData(1, 17, characterUnlock=True),
    ItemName.DWRoxas: ItemData(1, 19, characterUnlock=True),
}

Consumable_Table = {
    ItemName.Potion: ItemData(1, 0x0002),
    ItemName.HiPotion: ItemData(1, 0x0003),
    ItemName.MegaPotion: ItemData(1, 0x0004),
    ItemName.Ether: ItemData(1, 0x0005),
    ItemName.HiEther: ItemData(1, 0x0006),
    ItemName.MegaEther: ItemData(1, 0x0007),
    ItemName.Elixir: ItemData(1, 0x0008),
    ItemName.Megalixir: ItemData(1, 0x0009),
    ItemName.Panacea: ItemData(1, 0x000A),
    ItemName.LimitRecharge: ItemData(1, 0x000B),
}

Synthesis_Table = {
    ItemName.Bone: ItemData(1, 0x000C),
    ItemName.BlazingShard: ItemData(1, 0x000D),
    ItemName.BlazingGem: ItemData(1, 0x000F),
    ItemName.BlazingCrystal: ItemData(1, 0x0010),
    ItemName.FrostShard: ItemData(1, 0x0011),
    ItemName.FrostGem: ItemData(1, 0x0013),
    ItemName.FrostCrystal: ItemData(1, 0x0014),
    ItemName.LightningShard: ItemData(1, 0x0015),
    ItemName.LightningGem: ItemData(1, 0x0017),
    ItemName.LightningCrystal: ItemData(1, 0x0018),
    ItemName.FireRecipe: ItemData(1, 0x00FB),
    ItemName.FiraRecipe: ItemData(1, 0x00FC),
    ItemName.FiragaRecipe: ItemData(1, 0x00FD),
    ItemName.BlizzardRecipe: ItemData(1, 0x00FE),
    ItemName.BlizzaraRecipe: ItemData(1, 0x00FF),
    ItemName.BlizzagaRecipe: ItemData(1, 0x0100),
    ItemName.ThunderRecipe: ItemData(1, 0x0101),
    ItemName.ThundaraRecipe: ItemData(1, 0x0102),
    ItemName.ThundagaRecipe: ItemData(1, 0x0103),
    ItemName.AeroRecipe: ItemData(1, 0x0104),
    ItemName.AeroraRecipe: ItemData(1, 0x0105),
    ItemName.AerogaRecipe: ItemData(1, 0x0106),
    ItemName.CureRecipe: ItemData(1, 0x0107),
    ItemName.CuraRecipe: ItemData(1, 0x0108),
    ItemName.CuragaRecipe: ItemData(1, 0x0109),
    ItemName.GustShard: ItemData(1, 0x010A),
    ItemName.GustGem: ItemData(1, 0x010B),
    ItemName.GustCrystal: ItemData(1, 0x010C),
    ItemName.ShiningShard: ItemData(1, 0x010D),
    ItemName.ShiningGem: ItemData(1, 0x010E),
    ItemName.ShiningCrystal: ItemData(1, 0x010F),
    ItemName.GearComponentA: ItemData(1, 0x0110),
    ItemName.GearComponentB: ItemData(1, 0x0111),
    ItemName.GearComponentC: ItemData(1, 0x0112),
    ItemName.GearComponentD: ItemData(1, 0x0113),
    ItemName.ComboTech: ItemData(1, 0x0114),
    ItemName.RuneTech: ItemData(1, 0x0115),
    ItemName.PowerTech: ItemData(1, 0x0116),
    ItemName.AerialTech: ItemData(1, 0x0117),
    ItemName.RangeTech: ItemData(1, 0x0118),
    ItemName.ComboTechPlus: ItemData(1, 0x0119),
    ItemName.RuneTechPlus: ItemData(1, 0x011A),
    ItemName.PowerTechPlus: ItemData(1, 0x011B),
    ItemName.AerialTechPlus: ItemData(1, 0x011C),
    ItemName.RangeTechPlus: ItemData(1, 0x011D),
    ItemName.ComboTechPlus2: ItemData(1, 0x011E),
    ItemName.RuneTechPlus2: ItemData(1, 0x011F),
    ItemName.PowerTechPlus2: ItemData(1, 0x0120),
    ItemName.AerialTechPlus2: ItemData(1, 0x0121),
    ItemName.RangeTechPlus2: ItemData(1, 0x0122),
    ItemName.ShieldTech: ItemData(1, 0x012A),
    ItemName.ShieldTechPlus: ItemData(1, 0x012B),
    ItemName.LuckTech: ItemData(1, 0x012C),
    ItemName.ElixirRecipe: ItemData(1, 0x0131),
    ItemName.MegalixirRecipe: ItemData(1, 0x0132),
    ItemName.ShieldTechPlus2: ItemData(1, 0x0136),
    ItemName.Iron: ItemData(1, 0x0137),
    ItemName.Bronze: ItemData(1, 0x0138),
    ItemName.DarkIngot: ItemData(1, 0x0139),
    ItemName.Silver: ItemData(1, 0x013A),
    ItemName.Gold: ItemData(1, 0x013B),
    ItemName.Mithril: ItemData(1, 0x013C),
    ItemName.Orichalcum: ItemData(1, 0x013D),
    ItemName.Adamantite: ItemData(1, 0x013E),
    ItemName.Diamond: ItemData(1, 0x013F),
    ItemName.Moonstone: ItemData(1, 0x0140),
    ItemName.PremiumOrb: ItemData(1, 0x0141),
    ItemName.Ankharite: ItemData(1, 0x0143),
}

Unit_Table = {
    ItemName.AbilityUnit: ItemData(3, 0x00F1),
    ItemName.PowerUnit: ItemData(3, 0x00F7),
    ItemName.GuardUnit: ItemData(3, 0x00F8),
    ItemName.MagicUnit: ItemData(3, 0x00F9),
    ItemName.SightUnit: ItemData(3, 0x00FA),
}

Abillity_Table = {
    ItemName.DodgeRoll1: ItemData(1, 0x0075),
    ItemName.DodgeRoll2: ItemData(1, 0x0076),
    ItemName.DodgeRollLVPlus: ItemData(2, 0x0077),
    ItemName.DodgeRush: ItemData(1, 0x0078),
    ItemName.DodgeCombo: ItemData(1, 0x0079),
    ItemName.AutoDodge: ItemData(1, 0x007A),
    ItemName.Block1: ItemData(1, 0x007B),
    ItemName.Block2: ItemData(1, 0x007C),
    ItemName.BlockLVPlus: ItemData(2, 0x007D),
    ItemName.PerfectBlock: ItemData(1, 0x007E),
    ItemName.BlockCounter: ItemData(1, 0x007F),
    ItemName.BlockRetreat: ItemData(1, 0x0080),
    ItemName.SlidingBlock: ItemData(1, 0x0081),
    ItemName.BlockJump: ItemData(1, 0x0082),
    ItemName.FireBlock: ItemData(1, 0x0083),
    ItemName.BlizzardBlock: ItemData(1, 0x0084),
    ItemName.ThunderBlock: ItemData(1, 0x0085),
    ItemName.AeroBlock: ItemData(1, 0x0086),
    ItemName.BlockBonus: ItemData(1, 0x0087),
    ItemName.RoundBlock: ItemData(1, 0x0088),
    ItemName.AutoBlock: ItemData(1, 0x0089),
    ItemName.Glide1: ItemData(1, 0x008A),
    ItemName.Glide2: ItemData(1, 0x008B),
    ItemName.GlideLVPlus: ItemData(2, 0x008C),
    ItemName.HomingGlide: ItemData(1, 0x008E),
    ItemName.RocketGlide: ItemData(1, 0x008F),
    ItemName.AirSlide1: ItemData(1, 0x0090),
    ItemName.AirSlide2: ItemData(1, 0x0091),
    ItemName.AirSlideLVPlus: ItemData(2, 0x0092),
    ItemName.AirRush: ItemData(1, 0x0093),
    ItemName.AerialRecovery1: ItemData(1, 0x0094),
    ItemName.AerialRecovery2: ItemData(1, 0x0095),
    ItemName.ARecoveryLVPlus: ItemData(2, 0x0096),
    ItemName.QuickRecovery: ItemData(1, 0x0097),
    ItemName.AerialPayback: ItemData(1, 0x0098),
    ItemName.SmashRecovery: ItemData(1, 0x0099),
    ItemName.SlidingDash1: ItemData(1, 0x009A),
    ItemName.SlidingDash2: ItemData(1, 0x009B),
    ItemName.SlidingDashLVPlus: ItemData(2, 0x009C),
    ItemName.Haste1: ItemData(1, 0x009D),
    ItemName.Haste2: ItemData(1, 0x009E),
    ItemName.HasteLVPlus: ItemData(2, 0x009F),
    ItemName.HighJump1: ItemData(1, 0x00A0),
    ItemName.HighJump2: ItemData(1, 0x00A1),
    ItemName.HighJumpLVPlus: ItemData(2, 0x00A2),
    ItemName.Float: ItemData(1, 0x00A3),
    ItemName.AutoLife: ItemData(1, 0x00A4),
    ItemName.AutoLifeLVPlus: ItemData(2, 0x00A5),
    ItemName.TreasureMagnet1: ItemData(1, 0x00B4),
    ItemName.TreasureMagnet2: ItemData(1, 0x00B5),
    ItemName.TMagnetLVPlus: ItemData(2, 0x00B6),
    ItemName.RangeExtender: ItemData(1, 0x00BB),
    ItemName.Scan: ItemData(1, 0x00BC),
    ItemName.LimitBoost: ItemData(1, 0x00BD),
    ItemName.AutoLock: ItemData(1, 0x00BE),
    ItemName.UltimaWeapon: ItemData(1, 0x01BF),
    ItemName.DodgeDfl: ItemData(1, 0x01C0),
    ItemName.FinalLimit: ItemData(1, 0x01C1),
}

Accesories_Table = {
    ItemName.SorasAwakening: ItemData(1, 0x01C8),
    ItemName.TheKingsReturn: ItemData(1, 0x01C9),
    ItemName.SignofResolve: ItemData(1, 0x01CA),
    ItemName.BrawlRing: ItemData(1, 0x01CB),
    ItemName.MagicRing: ItemData(1, 0x01CC),
    ItemName.SoldierRing: ItemData(1, 0x01CD),
    ItemName.FencersRing: ItemData(1, 0x01CE),
    ItemName.FireCharm: ItemData(1, 0x01CF),
    ItemName.FlowerCharm: ItemData(1, 0x01D0),
    ItemName.StrikeRing: ItemData(1, 0x01D1),
    ItemName.LuckyRing: ItemData(1, 0x01D2),
    ItemName.BlizzardCharm: ItemData(1, 0x01D3),
    ItemName.WhiteRing: ItemData(1, 0x01D4),
    ItemName.KnightDef: ItemData(1, 0x01D5),
    ItemName.RaidersRing: ItemData(1, 0x01D6),
    ItemName.ThunderCharm: ItemData(1, 0x01D7),
    ItemName.RecoveryRing: ItemData(1, 0x01D8),
    ItemName.VitalityRing: ItemData(1, 0x01D9),
    ItemName.RainRing: ItemData(1, 0x01DA),
    ItemName.DoubleUp: ItemData(1, 0x01DB),
    ItemName.StormsEye: ItemData(1, 0x01DC),
    ItemName.CriticalRing: ItemData(1, 0x01DD),
    ItemName.FairyCircle: ItemData(1, 0x01DE),
    ItemName.FullCircle: ItemData(1, 0x01DF),
    ItemName.LuckyStar: ItemData(1, 0x01E0),
    ItemName.ChargeRing: ItemData(1, 0x01E1),
    ItemName.EternalRing: ItemData(1, 0x01E2),
    ItemName.CarmineBlight: ItemData(1, 0x01E3),
    ItemName.FrozenBlight: ItemData(1, 0x01E4),
    ItemName.SafetyRing: ItemData(1, 0x01E5),
    ItemName.PrincesssCrown: ItemData(1, 0x01E6),
    ItemName.LunarStrike: ItemData(1, 0x01E7),
    ItemName.CrimsonBlood: ItemData(1, 0x01E8),
    ItemName.DeepSky: ItemData(1, 0x01E9),
    ItemName.ProtectRing: ItemData(1, 0x01EA),
    ItemName.MightCrown: ItemData(1, 0x01EB),
    ItemName.CriticalSun: ItemData(1, 0x01EC),
    ItemName.ThreeStars: ItemData(1, 0x01ED),
    ItemName.ImperialCrown: ItemData(1, 0x01EE),
    ItemName.WitchsChaos: ItemData(1, 0x01EF),
    ItemName.RuneRing: ItemData(1, 0x01F0),
    ItemName.Extreme: ItemData(1, 0x01F1),
    ItemName.MastersCircle: ItemData(1, 0x01F2),
    ItemName.SpaceinItsPlace: ItemData(1, 0x01F3),
    ItemName.FlaggingWinds: ItemData(1, 0x01F4),
    ItemName.IceBreaker: ItemData(1, 0x01F5),
    ItemName.DowntoEarth: ItemData(1, 0x01F6),
    ItemName.LoseYourIllusion: ItemData(1, 0x01F7),
    ItemName.SighingoftheMoon: ItemData(1, 0x01F8),
    ItemName.TearsofFlame: ItemData(1, 0x01F9),
    ItemName.PartingofWaters: ItemData(1, 0x01FA),
    ItemName.TestofTime: ItemData(1, 0x01FB),
    ItemName.FlowersAthirst: ItemData(1, 0x01FC),
    ItemName.StolenThunder: ItemData(1, 0x01FD),
    ItemName.DyingoftheLight: ItemData(1, 0x01FE),
    ItemName.NothingtoFear: ItemData(1, 0x01FF),
}

Magic_Table = {
    ItemName.Fire: ItemData(3, 0x005D),
    ItemName.Fira: ItemData(3, 0x005E),
    ItemName.Firaga: ItemData(3, 0x005F),
    ItemName.Blizzard: ItemData(3, 0x0060),
    ItemName.Blizzara: ItemData(3, 0x0061),
    ItemName.Blizzaga: ItemData(3, 0x0062),
    ItemName.Thunder: ItemData(3, 0x0063),
    ItemName.Thundara: ItemData(3, 0x0064),
    ItemName.Thundaga: ItemData(3, 0x0065),
    ItemName.Aero: ItemData(3, 0x0066),
    ItemName.Aerora: ItemData(3, 0x0067),
    ItemName.Aeroga: ItemData(3, 0x0068),
    ItemName.Cure: ItemData(3, 0x0069),
    ItemName.Cura: ItemData(3, 0x006A),
    ItemName.Curaga: ItemData(3, 0x006B),
}

Magic_Enhancements_Table = {
    ItemName.MagicLV21: ItemData(1, 0x006C),
    ItemName.MagicLV22: ItemData(1, 0x006D),
    ItemName.MagicLV23: ItemData(1, 0x006E),
    ItemName.MagicLV32: ItemData(1, 0x006F),
    ItemName.MagicLV33: ItemData(1, 0x0070),
    ItemName.MagicLV42: ItemData(1, 0x0071),
    ItemName.Doublecast: ItemData(1, 0x0072),
    ItemName.Triplecast: ItemData(1, 0x0073),
    ItemName.Quadcast: ItemData(1, 0x0074),
}

Level_Table = {
    ItemName.LevelUp: ItemData(10, 0x003F),
    ItemName.LVDoubler2: ItemData(1, 0x0040),
    ItemName.LVDoubler3: ItemData(1, 0x0041),
    ItemName.LVTripler1: ItemData(1, 0x0042),
    ItemName.LVTripler2: ItemData(1, 0x0043),
    ItemName.LVTripler3: ItemData(1, 0x0044),
    ItemName.LVQuadrupler1: ItemData(1, 0x0045),
    ItemName.LVQuadrupler2: ItemData(1, 0x0046),
    ItemName.LVQuadrupler3: ItemData(1, 0x0047),
    ItemName.LVDoubler4: ItemData(1, 0x01C5),
    ItemName.LVDoubler5: ItemData(1, 0x01C6),
    ItemName.LVDoubler6: ItemData(1, 0x01C7),
}

Panel_Table = {
    ItemName.SlotReleaser: ItemData(20, 0x0001),
    ItemName.Backpack: ItemData(2, 0x005B),
    ItemName.PackExtender: ItemData(1, 0x005C),
    ItemName.LimitPass: ItemData(1, 0x01A0),
}

Badge_Table = {
    ItemName.OrdealBadge: ItemData(1, 0x01C2),
    ItemName.OrdealBlazon: ItemData(1, 0x01C3),
    ItemName.UnityBadge: ItemData(1, 0x01C4),
}

Goal_Table = {
    ItemName.SeaSaltIceCream : ItemData(1,0,seaSalt= True)
}
item_dictionary_table = {
    **Gear_Table,
    **Mission_Table,
    **Character_Table,
    **Consumable_Table,
    **Synthesis_Table,
    **Unit_Table,
    **Abillity_Table,
    **Accesories_Table,
    **Magic_Table,
    **Magic_Enhancements_Table,
    **Level_Table,
    **Panel_Table,
    **Badge_Table,
    **Goal_Table
}

progression_set = {
    item_name for keys in [
        Mission_Table.keys(),
        Magic_Table.keys(),
        Abillity_Table.keys(),
        Panel_Table.keys(),
        Goal_Table.keys()
    ]
    for item_name in keys
}

useful_set = {
    item_name for keys in [
    Level_Table.keys(),
    Magic_Enhancements_Table.keys(),
    Gear_Table.keys(),
    Character_Table.keys(),
    Unit_Table.keys(),
    Accesories_Table.keys()
    ]
    for item_name in keys

}

filler_set = {
    item_name for keys in [
    Consumable_Table.keys(),
    Synthesis_Table.keys(),
    Badge_Table.keys()
    ]
    for item_name in keys
}

# V2 item pool


GearTiers = {
    'Starter': (
        ItemName.SkillGear, ItemName.SkillGearPlus, ItemName.LoadedGear,
        ItemName.WildGear, ItemName.CasualGear,
    ),
    'Early': (
        ItemName.FearlessGear, ItemName.LiftGear, ItemName.LoadedGearPlus,
        ItemName.ValorGear, ItemName.TechnicalGear, ItemName.WildGearPlus,
        ItemName.ValorGearPlus, ItemName.FearlessGearPlus, ItemName.PrestigeGear,
        ItemName.LiftGearPlus, ItemName.DuelGear, ItemName.TechnicalGearPlus,
        ItemName.ChronoGear,
    ),
    'Midgame': (
        ItemName.PrestigeGearPlus, ItemName.NimbleGear, ItemName.OminGear,
        ItemName.ChronoGearPlus, ItemName.DuelGearPlus, ItemName.PhantomGear,
        ItemName.ChampionGear, ItemName.NimbleGearPlus, ItemName.OminGearP,
        ItemName.CrisisGear, ItemName.PhantomGearPlus,
    ),
    'Advanced': (
        ItemName.ChampionGearPlus, ItemName.MysteryGear, ItemName.DuelGearPlus2,
        ItemName.RageGear, ItemName.CrisisGearPlus, ItemName.PhantomGearPlus2,
        ItemName.RageGearPlus, ItemName.HazardGear, ItemName.OmegaGear,
        ItemName.UltimateGear,
    ),
    'Endgame': (
        ItemName.UltimateGearPlus, ItemName.PandorasGear, ItemName.HazardGearPlus,
        ItemName.OmegaGearPlus, ItemName.ZeroGear, ItemName.PandorasGearPlus,
    ),
}

GearDraws = {
    'Starter': (1, 1, 1),
    'Early': (1, 1, 1, 1, 1),
    'Midgame': (1, 1, 1, 1, 1, 2, 2, 2, 2),
    'Advanced': (1, 1, 1, 1, 2, 2, 2, 2),
    'Endgame': (2, 2, 2, 3, 3),
}

GearPacks = {
    'Progressive Gear': ItemData(30, 0x0300, pack=True),
}

AbilPacks = {
    'Progressive Treasure Magnet': ItemData(2, 0x0304, pack=True),
    'Progressive Sliding Dash': ItemData(2, 0x0305, pack=True),
    'Progressive Haste': ItemData(2, 0x0306, pack=True),
    'Progressive Auto-Life': ItemData(2, 0x0307, pack=True),
    'Progressive Glide': ItemData(2, 0x0308, pack=True),
    'Progressive Block': ItemData(2, 0x0309, pack=True),
    'Progressive Dodge Roll': ItemData(2, 0x030A, pack=True),
    'Progressive Air Slide': ItemData(2, 0x030B, pack=True),
    'Progressive Aerial Recovery': ItemData(2, 0x030C, pack=True),
    'Progressive High Jump': ItemData(2, 0x030D, pack=True),
    'Utility Glide Pack': ItemData(1, 0x030E, pack=True),
    'Counter Block Pack': ItemData(1, 0x030F, pack=True),
    'Elemental Block Pack': ItemData(1, 0x0310, pack=True),
    'Defensive Block Pack': ItemData(1, 0x0311, pack=True),
    'Utility Block Pack': ItemData(1, 0x0312, pack=True),
    'Offensive Dodge Pack': ItemData(1, 0x0313, pack=True),
    'Defensive Dodge Pack': ItemData(1, 0x0314, pack=True),
    'Lock on pack': ItemData(1, 0x0315, pack=True),
    'Limit Pack': ItemData(1, 0x0316, pack=True),
    'Utility Recovery Pack': ItemData(1, 0x0317, pack=True),
}


AccPacks = {
    'Progressive Strength Accessories': ItemData(4, 0x0318, pack=True),
    'Progressive Magic Accessories': ItemData(4, 0x0319, pack=True),
    'Progressive General Protection': ItemData(3, 0x031A, pack=True),
    'Progressive Healing and Item Support': ItemData(3, 0x031B, pack=True),
    'Progressive Elemental Protection': ItemData(4, 0x031C, pack=True),
    'Progressive Drops and Rewards': ItemData(3, 0x031D, pack=True),
    'Progressive EXP and Challenge': ItemData(2, 0x031E, pack=True),
    'Progressive Finishes': ItemData(4, 0x031F, pack=True),
}


UnitPacks = {
    'Progressive Units': ItemData(3, 0x0320, pack=True),
}


MagPacks = {
    'Fire bundle': ItemData(2, 0x0321, pack=True),
    'Fira bundle': ItemData(2, 0x0322, pack=True),
    'Firaga bundle': ItemData(2, 0x0323, pack=True),
    'Blizzard bundle': ItemData(2, 0x0324, pack=True),
    'Blizzara bundle': ItemData(2, 0x0325, pack=True),
    'Blizzaga bundle': ItemData(2, 0x0326, pack=True),
    'Thunder bundle': ItemData(2, 0x0327, pack=True),
    'Thundara bundle': ItemData(2, 0x0328, pack=True),
    'Thundaga bundle': ItemData(2, 0x0329, pack=True),
    'Aero bundle': ItemData(2, 0x032A, pack=True),
    'Aerora bundle': ItemData(2, 0x032B, pack=True),
    'Aeroga bundle': ItemData(2, 0x032C, pack=True),
    'Cure bundle': ItemData(2, 0x032D, pack=True),
    'Cura bundle': ItemData(2, 0x032E, pack=True),
    'Curaga bundle': ItemData(2, 0x032F, pack=True),
}


MagBoost = {
    'Progressive Magic Enhancements': ItemData(3, 0x0330, pack=True),
}


LvlPacks = {
    'Progressive Level Up': ItemData(4, 0x0331, pack=True),
}


PanelPacks = {
    'Panel Row Release': ItemData(20, 0x0332, pack=True),
    'Backpack pack': ItemData(1, 0x0333, pack=True),
}


Bundles = {
    'Progressive Treasure Magnet': (
        {ItemName.TreasureMagnet1: 1, ItemName.TMagnetLVPlus: 1},
        {ItemName.TreasureMagnet2: 1, ItemName.TMagnetLVPlus: 1},
    ),
    'Progressive Sliding Dash': (
        {ItemName.SlidingDash1: 1, ItemName.SlidingDashLVPlus: 1},
        {ItemName.SlidingDash2: 1, ItemName.SlidingDashLVPlus: 1},
    ),
    'Progressive Haste': ({ItemName.Haste1: 1, ItemName.HasteLVPlus: 1}, {ItemName.Haste2: 1, ItemName.HasteLVPlus: 1}),
    'Progressive Auto-Life': ({ItemName.AutoLife: 1}, {ItemName.AutoLifeLVPlus: 2}),
    'Progressive Glide': ({ItemName.Glide1: 1, ItemName.GlideLVPlus: 1}, {ItemName.Glide2: 1, ItemName.GlideLVPlus: 1}),
    'Progressive Block': ({ItemName.Block1: 1, ItemName.BlockLVPlus: 1}, {ItemName.Block2: 1, ItemName.BlockLVPlus: 1}),
    'Progressive Dodge Roll': ({ItemName.DodgeRoll1: 1, ItemName.DodgeRollLVPlus: 1}, {ItemName.DodgeRoll2: 1, ItemName.DodgeRollLVPlus: 1}),
    'Progressive Air Slide': (
        {ItemName.AirSlide1: 1, ItemName.AirSlideLVPlus: 1},
        {ItemName.AirSlide2: 1, ItemName.AirSlideLVPlus: 1, ItemName.AirRush: 1},
    ),
    'Progressive Aerial Recovery': (
        {ItemName.AerialRecovery1: 1, ItemName.ARecoveryLVPlus: 1},
        {ItemName.AerialRecovery2: 1, ItemName.ARecoveryLVPlus: 1},
    ),
    'Progressive High Jump': (
        {ItemName.HighJump1: 1, ItemName.HighJumpLVPlus: 1},
        {ItemName.HighJump2: 1, ItemName.HighJumpLVPlus: 1, ItemName.Float: 1},
    ),
    'Utility Glide Pack': ({ItemName.HomingGlide: 1, ItemName.RocketGlide: 1},),
    'Counter Block Pack': ({ItemName.BlockJump: 1, ItemName.BlockCounter: 1, ItemName.BlockRetreat: 1},),
    'Elemental Block Pack': ({ItemName.FireBlock: 1, ItemName.BlizzardBlock: 1, ItemName.ThunderBlock: 1, ItemName.AeroBlock: 1},),
    'Defensive Block Pack': ({ItemName.PerfectBlock: 1, ItemName.BlockBonus: 1, ItemName.AutoBlock: 1},),
    'Utility Block Pack': ({ItemName.SlidingBlock: 1, ItemName.RoundBlock: 1},),
    'Offensive Dodge Pack': ({ItemName.DodgeRush: 1, ItemName.DodgeCombo: 1},),
    'Defensive Dodge Pack': ({ItemName.AutoDodge: 1, ItemName.DodgeDfl: 1},),
    'Lock on pack': ({ItemName.RangeExtender: 1, ItemName.AutoLock: 1},),
    'Limit Pack': ({ItemName.LimitBoost: 1, ItemName.FinalLimit: 1},),
    'Utility Recovery Pack': ({ItemName.QuickRecovery: 1, ItemName.AerialPayback: 1, ItemName.SmashRecovery: 1},),
    'Progressive Strength Accessories': (
        {ItemName.SignofResolve: 1, ItemName.BrawlRing: 1, ItemName.FlowerCharm: 1, ItemName.SoldierRing: 1},
        {ItemName.StrikeRing: 1, ItemName.BlizzardCharm: 1, ItemName.RaidersRing: 1},
        {ItemName.EternalRing: 1, ItemName.CriticalRing: 1, ItemName.LunarStrike: 1},
        {ItemName.CrimsonBlood: 1, ItemName.CriticalSun: 1, ItemName.WitchsChaos: 1},
    ),
    'Progressive Magic Accessories': (
        {ItemName.MagicRing: 1},
        {ItemName.WhiteRing: 1},
        {ItemName.VitalityRing: 1},
        {ItemName.ImperialCrown: 1, ItemName.RuneRing: 1},
    ),
    'Progressive General Protection': (
        {ItemName.KnightDef: 1, ItemName.RecoveryRing: 1},
        {ItemName.FullCircle: 1, ItemName.PrincesssCrown: 1},
        {ItemName.ProtectRing: 1, ItemName.MightCrown: 1, ItemName.MastersCircle: 1},
    ),
    'Progressive Healing and Item Support': ({ItemName.FencersRing: 1}, {ItemName.ChargeRing: 1}, {ItemName.SafetyRing: 1}),
    'Progressive Elemental Protection': (
        {ItemName.FireCharm: 1, ItemName.ThunderCharm: 1, ItemName.IceBreaker: 1, ItemName.DowntoEarth: 1},
        {ItemName.StormsEye: 1, ItemName.TearsofFlame: 1, ItemName.PartingofWaters: 1, ItemName.FlaggingWinds: 1},
        {ItemName.FairyCircle: 1, ItemName.SpaceinItsPlace: 1, ItemName.LoseYourIllusion: 1, ItemName.TestofTime: 1},
        {ItemName.SighingoftheMoon: 1, ItemName.FlowersAthirst: 1, ItemName.StolenThunder: 1, ItemName.DyingoftheLight: 1, ItemName.NothingtoFear: 1},
    ),
    'Progressive Drops and Rewards': ({ItemName.LuckyRing: 1}, {ItemName.LuckyStar: 1}, {ItemName.ThreeStars: 1}),
    'Progressive EXP and Challenge': ({ItemName.DoubleUp: 1}, {ItemName.Extreme: 1}),
    'Progressive Finishes': ({ItemName.RainRing: 1}, {ItemName.CarmineBlight: 1}, {ItemName.FrozenBlight: 1}, {ItemName.DeepSky: 1}),
    'Progressive Units': (
        {ItemName.AbilityUnit: 1, ItemName.PowerUnit: 1, ItemName.GuardUnit: 1, ItemName.MagicUnit: 1, ItemName.SightUnit: 1},
    ),
    'Fire bundle': ({ItemName.Fire: 1},),
    'Fira bundle': ({ItemName.Fira: 1},),
    'Firaga bundle': ({ItemName.Firaga: 1},),
    'Blizzard bundle': ({ItemName.Blizzard: 1},),
    'Blizzara bundle': ({ItemName.Blizzara: 1},),
    'Blizzaga bundle': ({ItemName.Blizzaga: 1},),
    'Thunder bundle': ({ItemName.Thunder: 1},),
    'Thundara bundle': ({ItemName.Thundara: 1},),
    'Thundaga bundle': ({ItemName.Thundaga: 1},),
    'Aero bundle': ({ItemName.Aero: 1},),
    'Aerora bundle': ({ItemName.Aerora: 1},),
    'Aeroga bundle': ({ItemName.Aeroga: 1},),
    'Cure bundle': ({ItemName.Cure: 1},),
    'Cura bundle': ({ItemName.Cura: 1},),
    'Curaga bundle': ({ItemName.Curaga: 1},),
    'Progressive Magic Enhancements': (
        {ItemName.MagicLV21: 1, ItemName.Doublecast: 1},
        {ItemName.MagicLV32: 1, ItemName.Triplecast: 1},
        {ItemName.MagicLV42: 1, ItemName.Quadcast: 1},
    ),
    'Progressive Level Up': (
        {ItemName.LevelUp: 5, ItemName.LVDoubler2: 1},
        {ItemName.LevelUp: 5, ItemName.LVDoubler3: 1},
        {ItemName.LevelUp: 5, ItemName.LVTripler1: 1},
        {ItemName.LevelUp: 5, ItemName.LVQuadrupler1: 1},
    ),
    'Panel Row Release': ({ItemName.SlotReleaser: 1},),
    'Backpack pack': ({ItemName.Backpack: 2, ItemName.PackExtender: 1},),
}

V2Solo = {
    ItemName.Scan: Abillity_Table[ItemName.Scan],
    ItemName.UltimaWeapon: Abillity_Table[ItemName.UltimaWeapon],
    ItemName.LimitPass: Panel_Table[ItemName.LimitPass],
    ItemName.SorasAwakening: Accesories_Table[ItemName.SorasAwakening],
    ItemName.TheKingsReturn: Accesories_Table[ItemName.TheKingsReturn],
}

V2Items = {
    **GearPacks,
    **AbilPacks,
    **AccPacks,
    **UnitPacks,
    **MagPacks,
    **MagBoost,
    **LvlPacks,
    **PanelPacks,
    **V2Solo,
    **Mission_Table,
    **Character_Table,
    **Consumable_Table,
    **Synthesis_Table,
    **Badge_Table,
    **Goal_Table,
}

V2Prog = {
    item_name for keys in [
        ('Progressive Glide', 'Progressive High Jump', 'Progressive Air Slide', 'Panel Row Release'),
        GearPacks.keys(),
        MagPacks.keys(),
        Mission_Table.keys(),
        Character_Table.keys() - {ItemName.UnlockCharacterRoxas},
        Goal_Table.keys(),
    ]
    for item_name in keys
}

V2Useful = {
    item_name for keys in [
        GearPacks.keys(),
        AbilPacks.keys(),
        AccPacks.keys(),
        UnitPacks.keys(),
        MagPacks.keys(),
        MagBoost.keys(),
        LvlPacks.keys(),
        PanelPacks.keys(),
        V2Solo.keys(),
        Character_Table.keys(),
    ]
    for item_name in keys if item_name not in V2Prog
}

V2Filler = {
    item_name for keys in [
        Consumable_Table.keys(),
        Synthesis_Table.keys(),
        Badge_Table.keys(),
    ]
    for item_name in keys
}


class DaysItem(Item):
    game = "KH Days"
