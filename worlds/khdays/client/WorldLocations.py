import typing

from ..Names import LocationName


class WorldLocationData(typing.NamedTuple):
    mission: int
    kind: str
    slot: int


Mission1_Checks = {
    LocationName.Mission1Chest0: WorldLocationData(1, "Chest", 0),
    LocationName.Mission1Clear: WorldLocationData(1, "Clear", 0),
    LocationName.Mission1Clear2: WorldLocationData(1, "Clear", 1),
    LocationName.Mission1Clear3: WorldLocationData(1, "Clear", 2),
}

Mission2_Checks = {
    LocationName.Mission2Clear: WorldLocationData(2, "Clear", 0),
    LocationName.Mission2Clear2: WorldLocationData(2, "Clear", 1),
    LocationName.Mission2Clear3: WorldLocationData(2, "Clear", 2),
}

Mission3_Checks = {
    LocationName.Mission3Chest0: WorldLocationData(3, "Chest", 0),
    LocationName.Mission3Clear: WorldLocationData(3, "Clear", 0),
    LocationName.Mission3Clear2: WorldLocationData(3, "Clear", 1),
    LocationName.Mission3Clear3: WorldLocationData(3, "Clear", 2),
}

Mission4_Checks = {
    LocationName.Mission4Chest0: WorldLocationData(4, "Chest", 0),
    LocationName.Mission4Chest1: WorldLocationData(4, "Chest", 1),
    LocationName.Mission4Chest2: WorldLocationData(4, "Chest", 2),
    LocationName.Mission4Clear: WorldLocationData(4, "Clear", 0),
    LocationName.Mission4Clear2: WorldLocationData(4, "Clear", 1),
    LocationName.Mission4Clear3: WorldLocationData(4, "Clear", 2),
}

Mission5_Checks = {
    LocationName.Mission5Chest0: WorldLocationData(5, "Chest", 0),
    LocationName.Mission5Clear: WorldLocationData(5, "Clear", 0),
    LocationName.Mission5Clear2: WorldLocationData(5, "Clear", 1),
    LocationName.Mission5Clear3: WorldLocationData(5, "Clear", 2),
}

Mission6_Checks = {
    LocationName.Mission6Clear: WorldLocationData(6, "Clear", 0),
    LocationName.Mission6Clear2: WorldLocationData(6, "Clear", 1),
    LocationName.Mission6Clear3: WorldLocationData(6, "Clear", 2),
}

Mission7_Checks = {
    LocationName.Mission7Chest0: WorldLocationData(7, "Chest", 0),
    LocationName.Mission7Chest1: WorldLocationData(7, "Chest", 1),
    LocationName.Mission7Chest2: WorldLocationData(7, "Chest", 2),
    LocationName.Mission7Clear: WorldLocationData(7, "Clear", 0),
    LocationName.Mission7Clear2: WorldLocationData(7, "Clear", 1),
    LocationName.Mission7Clear3: WorldLocationData(7, "Clear", 2),
}

Mission8_Checks = {
    LocationName.Mission8Chest0: WorldLocationData(8, "Chest", 0),
    LocationName.Mission8Chest1: WorldLocationData(8, "Chest", 1),
    LocationName.Mission8Clear: WorldLocationData(8, "Clear", 0),
    LocationName.Mission8Clear2: WorldLocationData(8, "Clear", 1),
    LocationName.Mission8Clear3: WorldLocationData(8, "Clear", 2),
}

Mission9_Checks = {
    LocationName.Mission9Chest0: WorldLocationData(9, "Chest", 0),
    LocationName.Mission9Chest1: WorldLocationData(9, "Chest", 1),
    LocationName.Mission9Chest2: WorldLocationData(9, "Chest", 2),
    LocationName.Mission9Chest3: WorldLocationData(9, "Chest", 3),
    LocationName.Mission9Chest4: WorldLocationData(9, "Chest", 4),
    LocationName.Mission9Chest5: WorldLocationData(9, "Chest", 5),
    LocationName.Mission9Chest6: WorldLocationData(9, "Chest", 6),
    LocationName.Mission9Clear: WorldLocationData(9, "Clear", 0),
    LocationName.Mission9Clear2: WorldLocationData(9, "Clear", 1),
    LocationName.Mission9Clear3: WorldLocationData(9, "Clear", 2),
}

Mission10_Checks = {
    LocationName.Mission10Clear: WorldLocationData(10, "Clear", 0),
    LocationName.Mission10Clear2: WorldLocationData(10, "Clear", 1),
    LocationName.Mission10Clear3: WorldLocationData(10, "Clear", 2),
}

Mission11_Checks = {
    LocationName.Mission11Chest0: WorldLocationData(11, "Chest", 0),
    LocationName.Mission11Chest1: WorldLocationData(11, "Chest", 1),
    LocationName.Mission11Chest2: WorldLocationData(11, "Chest", 2),
    LocationName.Mission11Chest3: WorldLocationData(11, "Chest", 3),
    LocationName.Mission11Chest4: WorldLocationData(11, "Chest", 4),
    LocationName.Mission11Clear: WorldLocationData(11, "Clear", 0),
    LocationName.Mission11Clear2: WorldLocationData(11, "Clear", 1),
    LocationName.Mission11Clear3: WorldLocationData(11, "Clear", 2),
}

Mission12_Checks = {
    LocationName.Mission12Chest0: WorldLocationData(12, "Chest", 0),
    LocationName.Mission12Chest1: WorldLocationData(12, "Chest", 1),
    LocationName.Mission12Clear: WorldLocationData(12, "Clear", 0),
    LocationName.Mission12Clear2: WorldLocationData(12, "Clear", 1),
    LocationName.Mission12Clear3: WorldLocationData(12, "Clear", 2),
}

Mission13_Checks = {
    LocationName.Mission13Chest0: WorldLocationData(13, "Chest", 0),
    LocationName.Mission13Clear: WorldLocationData(13, "Clear", 0),
    LocationName.Mission13Clear2: WorldLocationData(13, "Clear", 1),
    LocationName.Mission13Clear3: WorldLocationData(13, "Clear", 2),
}

Mission14_Checks = {
    LocationName.Mission14Chest0: WorldLocationData(14, "Chest", 0),
    LocationName.Mission14Chest1: WorldLocationData(14, "Chest", 1),
    LocationName.Mission14Chest2: WorldLocationData(14, "Chest", 2),
    LocationName.Mission14Chest3: WorldLocationData(14, "Chest", 3),
    LocationName.Mission14Chest4: WorldLocationData(14, "Chest", 4),
    LocationName.Mission14Clear: WorldLocationData(14, "Clear", 0),
    LocationName.Mission14Clear2: WorldLocationData(14, "Clear", 1),
    LocationName.Mission14Clear3: WorldLocationData(14, "Clear", 2),
}

Mission15_Checks = {
    LocationName.Mission15Chest0: WorldLocationData(15, "Chest", 0),
    LocationName.Mission15Chest1: WorldLocationData(15, "Chest", 1),
    LocationName.Mission15Chest2: WorldLocationData(15, "Chest", 2),
    LocationName.Mission15Chest3: WorldLocationData(15, "Chest", 3),
    LocationName.Mission15Chest4: WorldLocationData(15, "Chest", 4),
    LocationName.Mission15Clear: WorldLocationData(15, "Clear", 0),
    LocationName.Mission15Clear2: WorldLocationData(15, "Clear", 1),
    LocationName.Mission15Clear3: WorldLocationData(15, "Clear", 2),
}

Mission16_Checks = {
    LocationName.Mission16Chest0: WorldLocationData(16, "Chest", 0),
    LocationName.Mission16Chest1: WorldLocationData(16, "Chest", 1),
    LocationName.Mission16Chest2: WorldLocationData(16, "Chest", 2),
    LocationName.Mission16Chest3: WorldLocationData(16, "Chest", 3),
    LocationName.Mission16Chest4: WorldLocationData(16, "Chest", 4),
    LocationName.Mission16Clear: WorldLocationData(16, "Clear", 0),
    LocationName.Mission16Clear2: WorldLocationData(16, "Clear", 1),
    LocationName.Mission16Clear3: WorldLocationData(16, "Clear", 2),
}

Mission17_Checks = {
    LocationName.Mission17Chest0: WorldLocationData(17, "Chest", 0),
    LocationName.Mission17Chest1: WorldLocationData(17, "Chest", 1),
    LocationName.Mission17Clear: WorldLocationData(17, "Clear", 0),
    LocationName.Mission17Clear2: WorldLocationData(17, "Clear", 1),
    LocationName.Mission17Clear3: WorldLocationData(17, "Clear", 2),
}

Mission18_Checks = {
    LocationName.Mission18Chest0: WorldLocationData(18, "Chest", 0),
    LocationName.Mission18Chest1: WorldLocationData(18, "Chest", 1),
    LocationName.Mission18Chest2: WorldLocationData(18, "Chest", 2),
    LocationName.Mission18Chest3: WorldLocationData(18, "Chest", 3),
    LocationName.Mission18Clear: WorldLocationData(18, "Clear", 0),
    LocationName.Mission18Clear2: WorldLocationData(18, "Clear", 1),
    LocationName.Mission18Clear3: WorldLocationData(18, "Clear", 2),
}

Mission19_Checks = {
    LocationName.Mission19Chest0: WorldLocationData(19, "Chest", 0),
    LocationName.Mission19Chest1: WorldLocationData(19, "Chest", 1),
    LocationName.Mission19Chest2: WorldLocationData(19, "Chest", 2),
    LocationName.Mission19Clear: WorldLocationData(19, "Clear", 0),
    LocationName.Mission19Clear2: WorldLocationData(19, "Clear", 1),
    LocationName.Mission19Clear3: WorldLocationData(19, "Clear", 2),
}

Mission20_Checks = {
    LocationName.Mission20Chest0: WorldLocationData(20, "Chest", 0),
    LocationName.Mission20Chest1: WorldLocationData(20, "Chest", 1),
    LocationName.Mission20Clear: WorldLocationData(20, "Clear", 0),
    LocationName.Mission20Clear2: WorldLocationData(20, "Clear", 1),
    LocationName.Mission20Clear3: WorldLocationData(20, "Clear", 2),
}

Mission21_Checks = {
    LocationName.Mission21Chest0: WorldLocationData(21, "Chest", 0),
    LocationName.Mission21Chest1: WorldLocationData(21, "Chest", 1),
    LocationName.Mission21Chest2: WorldLocationData(21, "Chest", 2),
    LocationName.Mission21Chest3: WorldLocationData(21, "Chest", 3),
    LocationName.Mission21Chest4: WorldLocationData(21, "Chest", 4),
    LocationName.Mission21Chest5: WorldLocationData(21, "Chest", 5),
    LocationName.Mission21Chest6: WorldLocationData(21, "Chest", 6),
    LocationName.Mission21Chest7: WorldLocationData(21, "Chest", 7),
    LocationName.Mission21Clear: WorldLocationData(21, "Clear", 0),
    LocationName.Mission21Clear2: WorldLocationData(21, "Clear", 1),
    LocationName.Mission21Clear3: WorldLocationData(21, "Clear", 2),
}

Mission22_Checks = {
    LocationName.Mission22Chest0: WorldLocationData(22, "Chest", 0),
    LocationName.Mission22Chest1: WorldLocationData(22, "Chest", 1),
    LocationName.Mission22Chest2: WorldLocationData(22, "Chest", 2),
    LocationName.Mission22Chest3: WorldLocationData(22, "Chest", 3),
    LocationName.Mission22Chest4: WorldLocationData(22, "Chest", 4),
    LocationName.Mission22Clear: WorldLocationData(22, "Clear", 0),
    LocationName.Mission22Clear2: WorldLocationData(22, "Clear", 1),
    LocationName.Mission22Clear3: WorldLocationData(22, "Clear", 2),
}

Mission23_Checks = {
    LocationName.Mission23Chest0: WorldLocationData(23, "Chest", 0),
    LocationName.Mission23Chest1: WorldLocationData(23, "Chest", 1),
    LocationName.Mission23Chest2: WorldLocationData(23, "Chest", 2),
    LocationName.Mission23Chest3: WorldLocationData(23, "Chest", 3),
    LocationName.Mission23Chest4: WorldLocationData(23, "Chest", 4),
    LocationName.Mission23Chest5: WorldLocationData(23, "Chest", 5),
    LocationName.Mission23Chest6: WorldLocationData(23, "Chest", 6),
    LocationName.Mission23Clear: WorldLocationData(23, "Clear", 0),
    LocationName.Mission23Clear2: WorldLocationData(23, "Clear", 1),
    LocationName.Mission23Clear3: WorldLocationData(23, "Clear", 2),
}

Mission24_Checks = {
    LocationName.Mission24Chest0: WorldLocationData(24, "Chest", 0),
    LocationName.Mission24Chest1: WorldLocationData(24, "Chest", 1),
    LocationName.Mission24Chest2: WorldLocationData(24, "Chest", 2),
    LocationName.Mission24Chest3: WorldLocationData(24, "Chest", 3),
    LocationName.Mission24Chest4: WorldLocationData(24, "Chest", 4),
    LocationName.Mission24Chest5: WorldLocationData(24, "Chest", 5),
    LocationName.Mission24Chest6: WorldLocationData(24, "Chest", 6),
    LocationName.Mission24Chest7: WorldLocationData(24, "Chest", 7),
    LocationName.Mission24Clear: WorldLocationData(24, "Clear", 0),
    LocationName.Mission24Clear2: WorldLocationData(24, "Clear", 1),
    LocationName.Mission24Clear3: WorldLocationData(24, "Clear", 2),
}

Mission25_Checks = {
    LocationName.Mission25Chest0: WorldLocationData(25, "Chest", 0),
    LocationName.Mission25Chest1: WorldLocationData(25, "Chest", 1),
    LocationName.Mission25Clear: WorldLocationData(25, "Clear", 0),
    LocationName.Mission25Clear2: WorldLocationData(25, "Clear", 1),
    LocationName.Mission25Clear3: WorldLocationData(25, "Clear", 2),
}

Mission26_Checks = {
    LocationName.Mission26Chest0: WorldLocationData(26, "Chest", 0),
    LocationName.Mission26Chest1: WorldLocationData(26, "Chest", 1),
    LocationName.Mission26Chest2: WorldLocationData(26, "Chest", 2),
    LocationName.Mission26Chest3: WorldLocationData(26, "Chest", 3),
    LocationName.Mission26Chest4: WorldLocationData(26, "Chest", 4),
    LocationName.Mission26Chest5: WorldLocationData(26, "Chest", 5),
    LocationName.Mission26Clear: WorldLocationData(26, "Clear", 0),
    LocationName.Mission26Clear2: WorldLocationData(26, "Clear", 1),
    LocationName.Mission26Clear3: WorldLocationData(26, "Clear", 2),
}

Mission27_Checks = {
    LocationName.Mission27Chest0: WorldLocationData(27, "Chest", 0),
    LocationName.Mission27Chest1: WorldLocationData(27, "Chest", 1),
    LocationName.Mission27Chest2: WorldLocationData(27, "Chest", 2),
    LocationName.Mission27Chest3: WorldLocationData(27, "Chest", 3),
    LocationName.Mission27Chest4: WorldLocationData(27, "Chest", 4),
    LocationName.Mission27Chest5: WorldLocationData(27, "Chest", 5),
    LocationName.Mission27Clear: WorldLocationData(27, "Clear", 0),
    LocationName.Mission27Clear2: WorldLocationData(27, "Clear", 1),
    LocationName.Mission27Clear3: WorldLocationData(27, "Clear", 2),
}

Mission28_Checks = {
    LocationName.Mission28Chest0: WorldLocationData(28, "Chest", 0),
    LocationName.Mission28Chest1: WorldLocationData(28, "Chest", 1),
    LocationName.Mission28Chest2: WorldLocationData(28, "Chest", 2),
    LocationName.Mission28Chest3: WorldLocationData(28, "Chest", 3),
    LocationName.Mission28Chest4: WorldLocationData(28, "Chest", 4),
    LocationName.Mission28Chest5: WorldLocationData(28, "Chest", 5),
    LocationName.Mission28Clear: WorldLocationData(28, "Clear", 0),
    LocationName.Mission28Clear2: WorldLocationData(28, "Clear", 1),
    LocationName.Mission28Clear3: WorldLocationData(28, "Clear", 2),
}

Mission29_Checks = {
    LocationName.Mission29Chest0: WorldLocationData(29, "Chest", 0),
    LocationName.Mission29Chest1: WorldLocationData(29, "Chest", 1),
    LocationName.Mission29Chest2: WorldLocationData(29, "Chest", 2),
    LocationName.Mission29Chest3: WorldLocationData(29, "Chest", 3),
    LocationName.Mission29Chest4: WorldLocationData(29, "Chest", 4),
    LocationName.Mission29Chest5: WorldLocationData(29, "Chest", 5),
    LocationName.Mission29Chest6: WorldLocationData(29, "Chest", 6),
    LocationName.Mission29Clear: WorldLocationData(29, "Clear", 0),
    LocationName.Mission29Clear2: WorldLocationData(29, "Clear", 1),
    LocationName.Mission29Clear3: WorldLocationData(29, "Clear", 2),
}

Mission30_Checks = {
    LocationName.Mission30Chest0: WorldLocationData(30, "Chest", 0),
    LocationName.Mission30Chest1: WorldLocationData(30, "Chest", 1),
    LocationName.Mission30Chest2: WorldLocationData(30, "Chest", 2),
    LocationName.Mission30Chest3: WorldLocationData(30, "Chest", 3),
    LocationName.Mission30Chest4: WorldLocationData(30, "Chest", 4),
    LocationName.Mission30Chest5: WorldLocationData(30, "Chest", 5),
    LocationName.Mission30Clear: WorldLocationData(30, "Clear", 0),
    LocationName.Mission30Clear2: WorldLocationData(30, "Clear", 1),
    LocationName.Mission30Clear3: WorldLocationData(30, "Clear", 2),
}

Mission31_Checks = {
    LocationName.Mission31Chest0: WorldLocationData(31, "Chest", 0),
    LocationName.Mission31Chest1: WorldLocationData(31, "Chest", 1),
    LocationName.Mission31Chest2: WorldLocationData(31, "Chest", 2),
    LocationName.Mission31Chest3: WorldLocationData(31, "Chest", 3),
    LocationName.Mission31Chest4: WorldLocationData(31, "Chest", 4),
    LocationName.Mission31Chest5: WorldLocationData(31, "Chest", 5),
    LocationName.Mission31Chest6: WorldLocationData(31, "Chest", 6),
    LocationName.Mission31Clear: WorldLocationData(31, "Clear", 0),
    LocationName.Mission31Clear2: WorldLocationData(31, "Clear", 1),
    LocationName.Mission31Clear3: WorldLocationData(31, "Clear", 2),
}

Mission32_Checks = {
    LocationName.Mission32Chest0: WorldLocationData(32, "Chest", 0),
    LocationName.Mission32Chest1: WorldLocationData(32, "Chest", 1),
    LocationName.Mission32Chest2: WorldLocationData(32, "Chest", 2),
    LocationName.Mission32Chest3: WorldLocationData(32, "Chest", 3),
    LocationName.Mission32Chest4: WorldLocationData(32, "Chest", 4),
    LocationName.Mission32Chest5: WorldLocationData(32, "Chest", 5),
    LocationName.Mission32Chest6: WorldLocationData(32, "Chest", 6),
    LocationName.Mission32Chest7: WorldLocationData(32, "Chest", 7),
    LocationName.Mission32Clear: WorldLocationData(32, "Clear", 0),
    LocationName.Mission32Clear2: WorldLocationData(32, "Clear", 1),
    LocationName.Mission32Clear3: WorldLocationData(32, "Clear", 2),
}

Mission33_Checks = {
    LocationName.Mission33Clear: WorldLocationData(33, "Clear", 0),
    LocationName.Mission33Clear2: WorldLocationData(33, "Clear", 1),
    LocationName.Mission33Clear3: WorldLocationData(33, "Clear", 2),
}

Mission34_Checks = {
    LocationName.Mission34Chest0: WorldLocationData(34, "Chest", 0),
    LocationName.Mission34Chest1: WorldLocationData(34, "Chest", 1),
    LocationName.Mission34Chest2: WorldLocationData(34, "Chest", 2),
    LocationName.Mission34Chest3: WorldLocationData(34, "Chest", 3),
    LocationName.Mission34Chest4: WorldLocationData(34, "Chest", 4),
    LocationName.Mission34Chest5: WorldLocationData(34, "Chest", 5),
    LocationName.Mission34Chest6: WorldLocationData(34, "Chest", 6),
    LocationName.Mission34Chest7: WorldLocationData(34, "Chest", 7),
    LocationName.Mission34Clear: WorldLocationData(34, "Clear", 0),
    LocationName.Mission34Clear2: WorldLocationData(34, "Clear", 1),
    LocationName.Mission34Clear3: WorldLocationData(34, "Clear", 2),
}

Mission35_Checks = {
    LocationName.Mission35Chest0: WorldLocationData(35, "Chest", 0),
    LocationName.Mission35Chest1: WorldLocationData(35, "Chest", 1),
    LocationName.Mission35Chest2: WorldLocationData(35, "Chest", 2),
    LocationName.Mission35Chest3: WorldLocationData(35, "Chest", 3),
    LocationName.Mission35Chest4: WorldLocationData(35, "Chest", 4),
    LocationName.Mission35Chest5: WorldLocationData(35, "Chest", 5),
    LocationName.Mission35Clear: WorldLocationData(35, "Clear", 0),
    LocationName.Mission35Clear2: WorldLocationData(35, "Clear", 1),
    LocationName.Mission35Clear3: WorldLocationData(35, "Clear", 2),
}

Mission36_Checks = {
    LocationName.Mission36Chest0: WorldLocationData(36, "Chest", 0),
    LocationName.Mission36Chest1: WorldLocationData(36, "Chest", 1),
    LocationName.Mission36Clear: WorldLocationData(36, "Clear", 0),
    LocationName.Mission36Clear2: WorldLocationData(36, "Clear", 1),
    LocationName.Mission36Clear3: WorldLocationData(36, "Clear", 2),
}

Mission37_Checks = {
    LocationName.Mission37Clear: WorldLocationData(37, "Clear", 0),
    LocationName.Mission37Clear2: WorldLocationData(37, "Clear", 1),
    LocationName.Mission37Clear3: WorldLocationData(37, "Clear", 2),
}

Mission38_Checks = {
    LocationName.Mission38Chest0: WorldLocationData(38, "Chest", 0),
    LocationName.Mission38Chest1: WorldLocationData(38, "Chest", 1),
    LocationName.Mission38Chest2: WorldLocationData(38, "Chest", 2),
    LocationName.Mission38Chest3: WorldLocationData(38, "Chest", 3),
    LocationName.Mission38Chest4: WorldLocationData(38, "Chest", 4),
    LocationName.Mission38Chest5: WorldLocationData(38, "Chest", 5),
    LocationName.Mission38Clear: WorldLocationData(38, "Clear", 0),
    LocationName.Mission38Clear2: WorldLocationData(38, "Clear", 1),
    LocationName.Mission38Clear3: WorldLocationData(38, "Clear", 2),
}

Mission39_Checks = {
    LocationName.Mission39Chest0: WorldLocationData(39, "Chest", 0),
    LocationName.Mission39Chest1: WorldLocationData(39, "Chest", 1),
    LocationName.Mission39Chest2: WorldLocationData(39, "Chest", 2),
    LocationName.Mission39Clear: WorldLocationData(39, "Clear", 0),
    LocationName.Mission39Clear2: WorldLocationData(39, "Clear", 1),
    LocationName.Mission39Clear3: WorldLocationData(39, "Clear", 2),
}

Mission40_Checks = {
    LocationName.Mission40Chest0: WorldLocationData(40, "Chest", 0),
    LocationName.Mission40Chest1: WorldLocationData(40, "Chest", 1),
    LocationName.Mission40Chest2: WorldLocationData(40, "Chest", 2),
    LocationName.Mission40Clear: WorldLocationData(40, "Clear", 0),
    LocationName.Mission40Clear2: WorldLocationData(40, "Clear", 1),
    LocationName.Mission40Clear3: WorldLocationData(40, "Clear", 2),
}

Mission41_Checks = {
    LocationName.Mission41Chest0: WorldLocationData(41, "Chest", 0),
    LocationName.Mission41Chest1: WorldLocationData(41, "Chest", 1),
    LocationName.Mission41Chest2: WorldLocationData(41, "Chest", 2),
    LocationName.Mission41Clear: WorldLocationData(41, "Clear", 0),
    LocationName.Mission41Clear2: WorldLocationData(41, "Clear", 1),
    LocationName.Mission41Clear3: WorldLocationData(41, "Clear", 2),
}

Mission42_Checks = {
    LocationName.Mission42Chest0: WorldLocationData(42, "Chest", 0),
    LocationName.Mission42Chest1: WorldLocationData(42, "Chest", 1),
    LocationName.Mission42Chest2: WorldLocationData(42, "Chest", 2),
    LocationName.Mission42Clear: WorldLocationData(42, "Clear", 0),
    LocationName.Mission42Clear2: WorldLocationData(42, "Clear", 1),
    LocationName.Mission42Clear3: WorldLocationData(42, "Clear", 2),
}

Mission43_Checks = {
    LocationName.Mission43Chest0: WorldLocationData(43, "Chest", 0),
    LocationName.Mission43Chest1: WorldLocationData(43, "Chest", 1),
    LocationName.Mission43Chest2: WorldLocationData(43, "Chest", 2),
    LocationName.Mission43Chest3: WorldLocationData(43, "Chest", 3),
    LocationName.Mission43Clear: WorldLocationData(43, "Clear", 0),
    LocationName.Mission43Clear2: WorldLocationData(43, "Clear", 1),
    LocationName.Mission43Clear3: WorldLocationData(43, "Clear", 2),
}

Mission44_Checks = {
    LocationName.Mission44Chest0: WorldLocationData(44, "Chest", 0),
    LocationName.Mission44Chest1: WorldLocationData(44, "Chest", 1),
    LocationName.Mission44Clear: WorldLocationData(44, "Clear", 0),
    LocationName.Mission44Clear2: WorldLocationData(44, "Clear", 1),
    LocationName.Mission44Clear3: WorldLocationData(44, "Clear", 2),
}

Mission45_Checks = {
    LocationName.Mission45Chest0: WorldLocationData(45, "Chest", 0),
    LocationName.Mission45Chest1: WorldLocationData(45, "Chest", 1),
    LocationName.Mission45Chest2: WorldLocationData(45, "Chest", 2),
    LocationName.Mission45Chest3: WorldLocationData(45, "Chest", 3),
    LocationName.Mission45Clear: WorldLocationData(45, "Clear", 0),
    LocationName.Mission45Clear2: WorldLocationData(45, "Clear", 1),
    LocationName.Mission45Clear3: WorldLocationData(45, "Clear", 2),
}

Mission46_Checks = {
    LocationName.Mission46Chest0: WorldLocationData(46, "Chest", 0),
    LocationName.Mission46Chest1: WorldLocationData(46, "Chest", 1),
    LocationName.Mission46Chest2: WorldLocationData(46, "Chest", 2),
    LocationName.Mission46Clear: WorldLocationData(46, "Clear", 0),
    LocationName.Mission46Clear2: WorldLocationData(46, "Clear", 1),
    LocationName.Mission46Clear3: WorldLocationData(46, "Clear", 2),
}

Mission47_Checks = {
    LocationName.Mission47Chest0: WorldLocationData(47, "Chest", 0),
    LocationName.Mission47Chest1: WorldLocationData(47, "Chest", 1),
    LocationName.Mission47Chest2: WorldLocationData(47, "Chest", 2),
    LocationName.Mission47Clear: WorldLocationData(47, "Clear", 0),
    LocationName.Mission47Clear2: WorldLocationData(47, "Clear", 1),
    LocationName.Mission47Clear3: WorldLocationData(47, "Clear", 2),
}

Mission48_Checks = {
    LocationName.Mission48Chest0: WorldLocationData(48, "Chest", 0),
    LocationName.Mission48Chest1: WorldLocationData(48, "Chest", 1),
    LocationName.Mission48Chest2: WorldLocationData(48, "Chest", 2),
    LocationName.Mission48Chest3: WorldLocationData(48, "Chest", 3),
    LocationName.Mission48Chest4: WorldLocationData(48, "Chest", 4),
    LocationName.Mission48Chest5: WorldLocationData(48, "Chest", 5),
    LocationName.Mission48Chest6: WorldLocationData(48, "Chest", 6),
    LocationName.Mission48Chest7: WorldLocationData(48, "Chest", 7),
    LocationName.Mission48Clear: WorldLocationData(48, "Clear", 0),
    LocationName.Mission48Clear2: WorldLocationData(48, "Clear", 1),
    LocationName.Mission48Clear3: WorldLocationData(48, "Clear", 2),
}

Mission49_Checks = {
    LocationName.Mission49Chest0: WorldLocationData(49, "Chest", 0),
    LocationName.Mission49Chest1: WorldLocationData(49, "Chest", 1),
    LocationName.Mission49Chest2: WorldLocationData(49, "Chest", 2),
    LocationName.Mission49Chest3: WorldLocationData(49, "Chest", 3),
    LocationName.Mission49Chest4: WorldLocationData(49, "Chest", 4),
    LocationName.Mission49Chest5: WorldLocationData(49, "Chest", 5),
    LocationName.Mission49Chest6: WorldLocationData(49, "Chest", 6),
    LocationName.Mission49Chest7: WorldLocationData(49, "Chest", 7),
    LocationName.Mission49Clear: WorldLocationData(49, "Clear", 0),
    LocationName.Mission49Clear2: WorldLocationData(49, "Clear", 1),
    LocationName.Mission49Clear3: WorldLocationData(49, "Clear", 2),
}

Mission50_Checks = {
    LocationName.Mission50Chest0: WorldLocationData(50, "Chest", 0),
    LocationName.Mission50Chest1: WorldLocationData(50, "Chest", 1),
    LocationName.Mission50Chest2: WorldLocationData(50, "Chest", 2),
    LocationName.Mission50Chest3: WorldLocationData(50, "Chest", 3),
    LocationName.Mission50Clear: WorldLocationData(50, "Clear", 0),
    LocationName.Mission50Clear2: WorldLocationData(50, "Clear", 1),
    LocationName.Mission50Clear3: WorldLocationData(50, "Clear", 2),
}

Mission51_Checks = {
    LocationName.Mission51Chest0: WorldLocationData(51, "Chest", 0),
    LocationName.Mission51Chest1: WorldLocationData(51, "Chest", 1),
    LocationName.Mission51Chest2: WorldLocationData(51, "Chest", 2),
    LocationName.Mission51Chest3: WorldLocationData(51, "Chest", 3),
    LocationName.Mission51Chest4: WorldLocationData(51, "Chest", 4),
    LocationName.Mission51Chest5: WorldLocationData(51, "Chest", 5),
    LocationName.Mission51Chest6: WorldLocationData(51, "Chest", 6),
    LocationName.Mission51Chest7: WorldLocationData(51, "Chest", 7),
    LocationName.Mission51Clear: WorldLocationData(51, "Clear", 0),
    LocationName.Mission51Clear2: WorldLocationData(51, "Clear", 1),
    LocationName.Mission51Clear3: WorldLocationData(51, "Clear", 2),
}

Mission52_Checks = {
    LocationName.Mission52Chest7: WorldLocationData(52, "Chest", 7),
    LocationName.Mission52Chest0: WorldLocationData(52, "Chest", 0),
    LocationName.Mission52Chest1: WorldLocationData(52, "Chest", 1),
    LocationName.Mission52Chest2: WorldLocationData(52, "Chest", 2),
    LocationName.Mission52Chest3: WorldLocationData(52, "Chest", 3),
    LocationName.Mission52Chest4: WorldLocationData(52, "Chest", 4),
    LocationName.Mission52Chest5: WorldLocationData(52, "Chest", 5),
    LocationName.Mission52Chest6: WorldLocationData(52, "Chest", 6),
    LocationName.Mission52Clear: WorldLocationData(52, "Clear", 0),
    LocationName.Mission52Clear2: WorldLocationData(52, "Clear", 1),
    LocationName.Mission52Clear3: WorldLocationData(52, "Clear", 2),
}

Mission53_Checks = {
    LocationName.Mission53Clear: WorldLocationData(53, "Clear", 0),
    LocationName.Mission53Clear2: WorldLocationData(53, "Clear", 1),
    LocationName.Mission53Clear3: WorldLocationData(53, "Clear", 2),
}

Mission54_Checks = {
    LocationName.Mission54Chest0: WorldLocationData(54, "Chest", 0),
    LocationName.Mission54Chest1: WorldLocationData(54, "Chest", 1),
    LocationName.Mission54Clear: WorldLocationData(54, "Clear", 0),
    LocationName.Mission54Clear2: WorldLocationData(54, "Clear", 1),
    LocationName.Mission54Clear3: WorldLocationData(54, "Clear", 2),
}

Mission55_Checks = {
    LocationName.Mission55Chest0: WorldLocationData(55, "Chest", 0),
    LocationName.Mission55Chest1: WorldLocationData(55, "Chest", 1),
    LocationName.Mission55Chest2: WorldLocationData(55, "Chest", 2),
    LocationName.Mission55Chest3: WorldLocationData(55, "Chest", 3),
    LocationName.Mission55Chest4: WorldLocationData(55, "Chest", 4),
    LocationName.Mission55Clear: WorldLocationData(55, "Clear", 0),
    LocationName.Mission55Clear2: WorldLocationData(55, "Clear", 1),
    LocationName.Mission55Clear3: WorldLocationData(55, "Clear", 2),
}

Mission56_Checks = {
    LocationName.Mission56Chest0: WorldLocationData(56, "Chest", 0),
    LocationName.Mission56Chest1: WorldLocationData(56, "Chest", 1),
    LocationName.Mission56Chest2: WorldLocationData(56, "Chest", 2),
    LocationName.Mission56Chest3: WorldLocationData(56, "Chest", 3),
    LocationName.Mission56Clear: WorldLocationData(56, "Clear", 0),
    LocationName.Mission56Clear2: WorldLocationData(56, "Clear", 1),
    LocationName.Mission56Clear3: WorldLocationData(56, "Clear", 2),
}

Mission57_Checks = {
    LocationName.Mission57Chest0: WorldLocationData(57, "Chest", 0),
    LocationName.Mission57Chest1: WorldLocationData(57, "Chest", 1),
    LocationName.Mission57Chest2: WorldLocationData(57, "Chest", 2),
    LocationName.Mission57Chest3: WorldLocationData(57, "Chest", 3),
    LocationName.Mission57Chest4: WorldLocationData(57, "Chest", 4),
    LocationName.Mission57Chest5: WorldLocationData(57, "Chest", 5),
    LocationName.Mission57Chest6: WorldLocationData(57, "Chest", 6),
    LocationName.Mission57Clear: WorldLocationData(57, "Clear", 0),
    LocationName.Mission57Clear2: WorldLocationData(57, "Clear", 1),
    LocationName.Mission57Clear3: WorldLocationData(57, "Clear", 2),
}

Mission58_Checks = {
    LocationName.Mission58Clear: WorldLocationData(58, "Clear", 0),
    LocationName.Mission58Clear2: WorldLocationData(58, "Clear", 1),
    LocationName.Mission58Clear3: WorldLocationData(58, "Clear", 2),
}

Mission59_Checks = {
    LocationName.Mission59Chest0: WorldLocationData(59, "Chest", 0),
    LocationName.Mission59Chest1: WorldLocationData(59, "Chest", 1),
    LocationName.Mission59Chest2: WorldLocationData(59, "Chest", 2),
    LocationName.Mission59Clear: WorldLocationData(59, "Clear", 0),
    LocationName.Mission59Clear2: WorldLocationData(59, "Clear", 1),
    LocationName.Mission59Clear3: WorldLocationData(59, "Clear", 2),
}

Mission60_Checks = {
    LocationName.Mission60Chest0: WorldLocationData(60, "Chest", 0),
    LocationName.Mission60Chest1: WorldLocationData(60, "Chest", 1),
    LocationName.Mission60Clear: WorldLocationData(60, "Clear", 0),
    LocationName.Mission60Clear2: WorldLocationData(60, "Clear", 1),
    LocationName.Mission60Clear3: WorldLocationData(60, "Clear", 2),
}

Mission61_Checks = {
    LocationName.Mission61Chest0: WorldLocationData(61, "Chest", 0),
    LocationName.Mission61Chest1: WorldLocationData(61, "Chest", 1),
    LocationName.Mission61Chest2: WorldLocationData(61, "Chest", 2),
    LocationName.Mission61Clear: WorldLocationData(61, "Clear", 0),
    LocationName.Mission61Clear2: WorldLocationData(61, "Clear", 1),
    LocationName.Mission61Clear3: WorldLocationData(61, "Clear", 2),
}

Mission62_Checks = {
    LocationName.Mission62Chest0: WorldLocationData(62, "Chest", 0),
    LocationName.Mission62Chest1: WorldLocationData(62, "Chest", 1),
    LocationName.Mission62Chest2: WorldLocationData(62, "Chest", 2),
    LocationName.Mission62Chest3: WorldLocationData(62, "Chest", 3),
    LocationName.Mission62Chest4: WorldLocationData(62, "Chest", 4),
    LocationName.Mission62Chest5: WorldLocationData(62, "Chest", 5),
    LocationName.Mission62Chest6: WorldLocationData(62, "Chest", 6),
    LocationName.Mission62Chest7: WorldLocationData(62, "Chest", 7),
    LocationName.Mission62Clear: WorldLocationData(62, "Clear", 0),
    LocationName.Mission62Clear2: WorldLocationData(62, "Clear", 1),
    LocationName.Mission62Clear3: WorldLocationData(62, "Clear", 2),
}

Mission63_Checks = {
    LocationName.Mission63Chest0: WorldLocationData(63, "Chest", 0),
    LocationName.Mission63Chest1: WorldLocationData(63, "Chest", 1),
    LocationName.Mission63Chest2: WorldLocationData(63, "Chest", 2),
    LocationName.Mission63Chest3: WorldLocationData(63, "Chest", 3),
    LocationName.Mission63Chest4: WorldLocationData(63, "Chest", 4),
    LocationName.Mission63Chest5: WorldLocationData(63, "Chest", 5),
    LocationName.Mission63Chest6: WorldLocationData(63, "Chest", 6),
    LocationName.Mission63Clear: WorldLocationData(63, "Clear", 0),
    LocationName.Mission63Clear2: WorldLocationData(63, "Clear", 1),
    LocationName.Mission63Clear3: WorldLocationData(63, "Clear", 2),
}

Mission64_Checks = {
    LocationName.Mission64Chest0: WorldLocationData(64, "Chest", 0),
    LocationName.Mission64Chest1: WorldLocationData(64, "Chest", 1),
    LocationName.Mission64Clear: WorldLocationData(64, "Clear", 0),
    LocationName.Mission64Clear2: WorldLocationData(64, "Clear", 1),
    LocationName.Mission64Clear3: WorldLocationData(64, "Clear", 2),
}

Mission65_Checks = {
    LocationName.Mission65Chest0: WorldLocationData(65, "Chest", 0),
    LocationName.Mission65Chest1: WorldLocationData(65, "Chest", 1),
    LocationName.Mission65Chest2: WorldLocationData(65, "Chest", 2),
    LocationName.Mission65Chest3: WorldLocationData(65, "Chest", 3),
    LocationName.Mission65Chest4: WorldLocationData(65, "Chest", 4),
    LocationName.Mission65Chest5: WorldLocationData(65, "Chest", 5),
    LocationName.Mission65Chest6: WorldLocationData(65, "Chest", 6),
    LocationName.Mission65Chest7: WorldLocationData(65, "Chest", 7),
    LocationName.Mission65Clear: WorldLocationData(65, "Clear", 0),
    LocationName.Mission65Clear2: WorldLocationData(65, "Clear", 1),
    LocationName.Mission65Clear3: WorldLocationData(65, "Clear", 2),
}

Mission66_Checks = {
    LocationName.Mission66Chest0: WorldLocationData(66, "Chest", 0),
    LocationName.Mission66Chest1: WorldLocationData(66, "Chest", 1),
    LocationName.Mission66Chest2: WorldLocationData(66, "Chest", 2),
    LocationName.Mission66Chest3: WorldLocationData(66, "Chest", 3),
    LocationName.Mission66Chest4: WorldLocationData(66, "Chest", 4),
    LocationName.Mission66Chest5: WorldLocationData(66, "Chest", 5),
    LocationName.Mission66Chest6: WorldLocationData(66, "Chest", 6),
    LocationName.Mission66Chest7: WorldLocationData(66, "Chest", 7),
    LocationName.Mission66Clear: WorldLocationData(66, "Clear", 0),
    LocationName.Mission66Clear2: WorldLocationData(66, "Clear", 1),
    LocationName.Mission66Clear3: WorldLocationData(66, "Clear", 2),
}

Mission67_Checks = {
    LocationName.Mission67Chest0: WorldLocationData(67, "Chest", 0),
    LocationName.Mission67Chest1: WorldLocationData(67, "Chest", 1),
    LocationName.Mission67Chest2: WorldLocationData(67, "Chest", 2),
    LocationName.Mission67Chest3: WorldLocationData(67, "Chest", 3),
    LocationName.Mission67Chest4: WorldLocationData(67, "Chest", 4),
    LocationName.Mission67Chest5: WorldLocationData(67, "Chest", 5),
    LocationName.Mission67Chest6: WorldLocationData(67, "Chest", 6),
    LocationName.Mission67Clear: WorldLocationData(67, "Clear", 0),
    LocationName.Mission67Clear2: WorldLocationData(67, "Clear", 1),
    LocationName.Mission67Clear3: WorldLocationData(67, "Clear", 2),
}

Mission68_Checks = {
    LocationName.Mission68Chest0: WorldLocationData(68, "Chest", 0),
    LocationName.Mission68Chest1: WorldLocationData(68, "Chest", 1),
    LocationName.Mission68Chest2: WorldLocationData(68, "Chest", 2),
    LocationName.Mission68Chest3: WorldLocationData(68, "Chest", 3),
    LocationName.Mission68Chest4: WorldLocationData(68, "Chest", 4),
    LocationName.Mission68Chest5: WorldLocationData(68, "Chest", 5),
    LocationName.Mission68Chest6: WorldLocationData(68, "Chest", 6),
    LocationName.Mission68Chest7: WorldLocationData(68, "Chest", 7),
    LocationName.Mission68Clear: WorldLocationData(68, "Clear", 0),
    LocationName.Mission68Clear2: WorldLocationData(68, "Clear", 1),
    LocationName.Mission68Clear3: WorldLocationData(68, "Clear", 2),
}

Mission69_Checks = {
    LocationName.Mission69Chest0: WorldLocationData(69, "Chest", 0),
    LocationName.Mission69Chest1: WorldLocationData(69, "Chest", 1),
    LocationName.Mission69Chest2: WorldLocationData(69, "Chest", 2),
    LocationName.Mission69Clear: WorldLocationData(69, "Clear", 0),
    LocationName.Mission69Clear2: WorldLocationData(69, "Clear", 1),
    LocationName.Mission69Clear3: WorldLocationData(69, "Clear", 2),
}

Mission70_Checks = {
    LocationName.Mission70Chest0: WorldLocationData(70, "Chest", 0),
    LocationName.Mission70Clear: WorldLocationData(70, "Clear", 0),
    LocationName.Mission70Clear2: WorldLocationData(70, "Clear", 1),
    LocationName.Mission70Clear3: WorldLocationData(70, "Clear", 2),
}

Mission71_Checks = {
    LocationName.Mission71Clear: WorldLocationData(71, "Clear", 0),
    LocationName.Mission71Clear2: WorldLocationData(71, "Clear", 1),
    LocationName.Mission71Clear3: WorldLocationData(71, "Clear", 2),
}

Mission72_Checks = {
    LocationName.Mission72Chest0: WorldLocationData(72, "Chest", 0),
    LocationName.Mission72Clear: WorldLocationData(72, "Clear", 0),
    LocationName.Mission72Clear2: WorldLocationData(72, "Clear", 1),
    LocationName.Mission72Clear3: WorldLocationData(72, "Clear", 2),
}

Mission73_Checks = {
    LocationName.Mission73Chest0: WorldLocationData(73, "Chest", 0),
    LocationName.Mission73Chest1: WorldLocationData(73, "Chest", 1),
    LocationName.Mission73Clear: WorldLocationData(73, "Clear", 0),
    LocationName.Mission73Clear2: WorldLocationData(73, "Clear", 1),
    LocationName.Mission73Clear3: WorldLocationData(73, "Clear", 2),
}

Mission74_Checks = {
    LocationName.Mission74Chest0: WorldLocationData(74, "Chest", 0),
    LocationName.Mission74Chest1: WorldLocationData(74, "Chest", 1),
    LocationName.Mission74Chest2: WorldLocationData(74, "Chest", 2),
    LocationName.Mission74Clear: WorldLocationData(74, "Clear", 0),
    LocationName.Mission74Clear2: WorldLocationData(74, "Clear", 1),
    LocationName.Mission74Clear3: WorldLocationData(74, "Clear", 2),
}

Mission75_Checks = {
    LocationName.Mission75Chest0: WorldLocationData(75, "Chest", 0),
    LocationName.Mission75Chest1: WorldLocationData(75, "Chest", 1),
    LocationName.Mission75Chest2: WorldLocationData(75, "Chest", 2),
    LocationName.Mission75Clear: WorldLocationData(75, "Clear", 0),
    LocationName.Mission75Clear2: WorldLocationData(75, "Clear", 1),
    LocationName.Mission75Clear3: WorldLocationData(75, "Clear", 2),
}

Mission76_Checks = {
    LocationName.Mission76Chest0: WorldLocationData(76, "Chest", 0),
    LocationName.Mission76Chest1: WorldLocationData(76, "Chest", 1),
    LocationName.Mission76Clear: WorldLocationData(76, "Clear", 0),
    LocationName.Mission76Clear2: WorldLocationData(76, "Clear", 1),
    LocationName.Mission76Clear3: WorldLocationData(76, "Clear", 2),
}

Mission77_Checks = {
    LocationName.Mission77Clear: WorldLocationData(77, "Clear", 0),
    LocationName.Mission77Clear2: WorldLocationData(77, "Clear", 1),
    LocationName.Mission77Clear3: WorldLocationData(77, "Clear", 2),
}

Mission78_Checks = {
    LocationName.Mission78Clear: WorldLocationData(78, "Clear", 0),
    LocationName.Mission78Clear2: WorldLocationData(78, "Clear", 1),
    LocationName.Mission78Clear3: WorldLocationData(78, "Clear", 2),
}

Mission79_Checks = {
    LocationName.Mission79Chest0: WorldLocationData(79, "Chest", 0),
    LocationName.Mission79Chest1: WorldLocationData(79, "Chest", 1),
    LocationName.Mission79Chest2: WorldLocationData(79, "Chest", 2),
    LocationName.Mission79Chest3: WorldLocationData(79, "Chest", 3),
    LocationName.Mission79Clear: WorldLocationData(79, "Clear", 0),
    LocationName.Mission79Clear2: WorldLocationData(79, "Clear", 1),
    LocationName.Mission79Clear3: WorldLocationData(79, "Clear", 2),
}

Mission80_Checks = {
    LocationName.Mission80Clear: WorldLocationData(80, "Clear", 0),
    LocationName.Mission80Clear2: WorldLocationData(80, "Clear", 1),
    LocationName.Mission80Clear3: WorldLocationData(80, "Clear", 2),
}

Mission81_Checks = {
    LocationName.Mission81Chest0: WorldLocationData(81, "Chest", 0),
    LocationName.Mission81Chest1: WorldLocationData(81, "Chest", 1),
    LocationName.Mission81Chest2: WorldLocationData(81, "Chest", 2),
    LocationName.Mission81Chest3: WorldLocationData(81, "Chest", 3),
    LocationName.Mission81Chest4: WorldLocationData(81, "Chest", 4),
    LocationName.Mission81Chest5: WorldLocationData(81, "Chest", 5),
    LocationName.Mission81Clear: WorldLocationData(81, "Clear", 0),
    LocationName.Mission81Clear2: WorldLocationData(81, "Clear", 1),
    LocationName.Mission81Clear3: WorldLocationData(81, "Clear", 2),
}

Mission82_Checks = {
    LocationName.Mission82Chest0: WorldLocationData(82, "Chest", 0),
    LocationName.Mission82Chest1: WorldLocationData(82, "Chest", 1),
    LocationName.Mission82Chest2: WorldLocationData(82, "Chest", 2),
    LocationName.Mission82Chest3: WorldLocationData(82, "Chest", 3),
    LocationName.Mission82Chest4: WorldLocationData(82, "Chest", 4),
    LocationName.Mission82Chest5: WorldLocationData(82, "Chest", 5),
    LocationName.Mission82Chest6: WorldLocationData(82, "Chest", 6),
    LocationName.Mission82Chest7: WorldLocationData(82, "Chest", 7),
    LocationName.Mission82Clear: WorldLocationData(82, "Clear", 0),
    LocationName.Mission82Clear2: WorldLocationData(82, "Clear", 1),
    LocationName.Mission82Clear3: WorldLocationData(82, "Clear", 2),
}

Mission83_Checks = {
    LocationName.Mission83Chest0: WorldLocationData(83, "Chest", 0),
    LocationName.Mission83Chest1: WorldLocationData(83, "Chest", 1),
    LocationName.Mission83Chest2: WorldLocationData(83, "Chest", 2),
    LocationName.Mission83Chest3: WorldLocationData(83, "Chest", 3),
    LocationName.Mission83Chest4: WorldLocationData(83, "Chest", 4),
    LocationName.Mission83Chest5: WorldLocationData(83, "Chest", 5),
    LocationName.Mission83Chest6: WorldLocationData(83, "Chest", 6),
    LocationName.Mission83Chest7: WorldLocationData(83, "Chest", 7),
    LocationName.Mission83Clear: WorldLocationData(83, "Clear", 0),
    LocationName.Mission83Clear2: WorldLocationData(83, "Clear", 1),
    LocationName.Mission83Clear3: WorldLocationData(83, "Clear", 2),
}

Mission84_Checks = {
    LocationName.Mission84Chest0: WorldLocationData(84, "Chest", 0),
    LocationName.Mission84Clear: WorldLocationData(84, "Clear", 0),
    LocationName.Mission84Clear2: WorldLocationData(84, "Clear", 1),
    LocationName.Mission84Clear3: WorldLocationData(84, "Clear", 2),
}

Mission85_Checks = {
    LocationName.Mission85Chest0: WorldLocationData(85, "Chest", 0),
    LocationName.Mission85Chest1: WorldLocationData(85, "Chest", 1),
    LocationName.Mission85Chest2: WorldLocationData(85, "Chest", 2),
    LocationName.Mission85Chest3: WorldLocationData(85, "Chest", 3),
    LocationName.Mission85Clear: WorldLocationData(85, "Clear", 0),
    LocationName.Mission85Clear2: WorldLocationData(85, "Clear", 1),
    LocationName.Mission85Clear3: WorldLocationData(85, "Clear", 2),
}

Mission86_Checks = {
    LocationName.Mission86Chest0: WorldLocationData(86, "Chest", 0),
    LocationName.Mission86Clear: WorldLocationData(86, "Clear", 0),
    LocationName.Mission86Clear2: WorldLocationData(86, "Clear", 1),
    LocationName.Mission86Clear3: WorldLocationData(86, "Clear", 2),
}

Mission87_Checks = {
    LocationName.Mission87Chest0: WorldLocationData(87, "Chest", 0),
    LocationName.Mission87Chest1: WorldLocationData(87, "Chest", 1),
    LocationName.Mission87Chest2: WorldLocationData(87, "Chest", 2),
    LocationName.Mission87Chest3: WorldLocationData(87, "Chest", 3),
    LocationName.Mission87Chest4: WorldLocationData(87, "Chest", 4),
    LocationName.Mission87Clear: WorldLocationData(87, "Clear", 0),
    LocationName.Mission87Clear2: WorldLocationData(87, "Clear", 1),
    LocationName.Mission87Clear3: WorldLocationData(87, "Clear", 2),
}

Mission88_Checks = {
    LocationName.Mission88Chest0: WorldLocationData(88, "Chest", 0),
    LocationName.Mission88Clear: WorldLocationData(88, "Clear", 0),
    LocationName.Mission88Clear2: WorldLocationData(88, "Clear", 1),
    LocationName.Mission88Clear3: WorldLocationData(88, "Clear", 2),
}

Mission89_Checks = {
    LocationName.Mission89Chest0: WorldLocationData(89, "Chest", 0),
    LocationName.Mission89Chest1: WorldLocationData(89, "Chest", 1),
    LocationName.Mission89Chest2: WorldLocationData(89, "Chest", 2),
    LocationName.Mission89Chest3: WorldLocationData(89, "Chest", 3),
    LocationName.Mission89Chest4: WorldLocationData(89, "Chest", 4),
    LocationName.Mission89Chest5: WorldLocationData(89, "Chest", 5),
    LocationName.Mission89Chest6: WorldLocationData(89, "Chest", 6),
    LocationName.Mission89Chest7: WorldLocationData(89, "Chest", 7),
    LocationName.Mission89Clear: WorldLocationData(89, "Clear", 0),
    LocationName.Mission89Clear2: WorldLocationData(89, "Clear", 1),
    LocationName.Mission89Clear3: WorldLocationData(89, "Clear", 2),
}

Mission90_Checks = {
    LocationName.Mission90Chest0: WorldLocationData(90, "Chest", 0),
    LocationName.Mission90Chest1: WorldLocationData(90, "Chest", 1),
    LocationName.Mission90Chest2: WorldLocationData(90, "Chest", 2),
    LocationName.Mission90Chest3: WorldLocationData(90, "Chest", 3),
    LocationName.Mission90Chest4: WorldLocationData(90, "Chest", 4),
    LocationName.Mission90Clear: WorldLocationData(90, "Clear", 0),
    LocationName.Mission90Clear2: WorldLocationData(90, "Clear", 1),
    LocationName.Mission90Clear3: WorldLocationData(90, "Clear", 2),
}

Mission91_Checks = {
    LocationName.Mission91Chest0: WorldLocationData(91, "Chest", 0),
    LocationName.Mission91Chest1: WorldLocationData(91, "Chest", 1),
    LocationName.Mission91Clear: WorldLocationData(91, "Clear", 0),
    LocationName.Mission91Clear2: WorldLocationData(91, "Clear", 1),
    LocationName.Mission91Clear3: WorldLocationData(91, "Clear", 2),
}

mission_locations = {
    1: Mission1_Checks,
    2: Mission2_Checks,
    3: Mission3_Checks,
    4: Mission4_Checks,
    5: Mission5_Checks,
    6: Mission6_Checks,
    7: Mission7_Checks,
    8: Mission8_Checks,
    9: Mission9_Checks,
    10: Mission10_Checks,
    11: Mission11_Checks,
    12: Mission12_Checks,
    13: Mission13_Checks,
    14: Mission14_Checks,
    15: Mission15_Checks,
    16: Mission16_Checks,
    17: Mission17_Checks,
    18: Mission18_Checks,
    19: Mission19_Checks,
    20: Mission20_Checks,
    21: Mission21_Checks,
    22: Mission22_Checks,
    23: Mission23_Checks,
    24: Mission24_Checks,
    25: Mission25_Checks,
    26: Mission26_Checks,
    27: Mission27_Checks,
    28: Mission28_Checks,
    29: Mission29_Checks,
    30: Mission30_Checks,
    31: Mission31_Checks,
    32: Mission32_Checks,
    33: Mission33_Checks,
    34: Mission34_Checks,
    35: Mission35_Checks,
    36: Mission36_Checks,
    37: Mission37_Checks,
    38: Mission38_Checks,
    39: Mission39_Checks,
    40: Mission40_Checks,
    41: Mission41_Checks,
    42: Mission42_Checks,
    43: Mission43_Checks,
    44: Mission44_Checks,
    45: Mission45_Checks,
    46: Mission46_Checks,
    47: Mission47_Checks,
    48: Mission48_Checks,
    49: Mission49_Checks,
    50: Mission50_Checks,
    51: Mission51_Checks,
    52: Mission52_Checks,
    53: Mission53_Checks,
    54: Mission54_Checks,
    55: Mission55_Checks,
    56: Mission56_Checks,
    57: Mission57_Checks,
    58: Mission58_Checks,
    59: Mission59_Checks,
    60: Mission60_Checks,
    61: Mission61_Checks,
    62: Mission62_Checks,
    63: Mission63_Checks,
    64: Mission64_Checks,
    65: Mission65_Checks,
    66: Mission66_Checks,
    67: Mission67_Checks,
    68: Mission68_Checks,
    69: Mission69_Checks,
    70: Mission70_Checks,
    71: Mission71_Checks,
    72: Mission72_Checks,
    73: Mission73_Checks,
    74: Mission74_Checks,
    75: Mission75_Checks,
    76: Mission76_Checks,
    77: Mission77_Checks,
    78: Mission78_Checks,
    79: Mission79_Checks,
    80: Mission80_Checks,
    81: Mission81_Checks,
    82: Mission82_Checks,
    83: Mission83_Checks,
    84: Mission84_Checks,
    85: Mission85_Checks,
    86: Mission86_Checks,
    87: Mission87_Checks,
    88: Mission88_Checks,
    89: Mission89_Checks,
    90: Mission90_Checks,
    91: Mission91_Checks,
}

all_world_locations = {
    name: data
    for checks in mission_locations.values()
    for name, data in checks.items()
}
