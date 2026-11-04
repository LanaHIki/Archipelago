# KH Days Archipelago Lua mod

Experimental: the transport, commands and gameplay polling are implemented. Clean-upstream Story Mode testing has verified AP connectivity, inventory, startup, Holo-Mission filtering, mission entry, bundles and reconnects. The checks below still need live verification before a seed playthrough.

This is a standalone mod for Yokimitsuro/khdays-port, requiring Lua API 2 with the memory API. It does not require the experimental C connector, AP source hooks, or a modified native executable.

Copy this folder to `mods/archipelago` beside the upstream game. Keep `mod.ini` and `scripts/` together. In the Days AP client, run:

```text
/native "C:/path/to/game/saves/mods/archipelago.khdays"
```

Connect to the AP server as usual. The mailbox directory follows the port's save profile; use the directory for the running player instance. Do not copy mailbox files into the mod's `data/` directory, because shipped data takes precedence over saved files.

The client writes `client.txt`; Lua writes `game.txt`. Both use ASCII headers and sequenced hexadecimal packets. Input contains a connection ID, acknowledged event number, then command lines. Output contains the connection ID, acknowledged command number, last event number, then event lines. Commands and events remain pending until acknowledged. A reconnect uses a new connection ID and replays unacknowledged events. Lua's output retains command acknowledgements over script reloads. Settings persist separately in `settings.txt`. Lua processes one command and publishes queued replies once per frame to stay within the port's 8 ms allowance. A temporary Windows file-sharing conflict leaves publication pending for retry.

The protocol carries the existing MelonMix packets, so AP item bundles, inventory reconciliation, mission unlocks, character settings, location handling and goal options use the existing APWorld logic. Lua applies their game effects with the memory API. An additional `0x12` ready packet asks the client to reconcile inventory after a save becomes available. Each inventory reply starts with `0x13`: its four-byte command sequence and ASCII connection ID. Reconciliation accepts only the matching query's completed inventory, preventing stale replies from causing duplicate grants.

The final gate holds the recognized Yes/No prompt on No while locked. This adapts the MelonMix input write to upstream Lua's end-of-frame timing: the next pad sample would overwrite a simulated A press before the menu reads it. Unlocking releases the cursor. The mod also suppresses a false initial mission check when the result record is first initialized.

## Verification

`test/test_native_bridge.py` runs Python against the actual Lua transport with file API stubs. It checks binary packets, acknowledgement pruning, duplicate command suppression, script reload, reconnect replay, asynchronous reads/drains and shutdown. `test/native_gameplay.lua` checks item grants, inventory packets, character assignment, flashback exceptions, the startup jump, result flags and withdrawal, the final gate, mission/day visibility, chests and scaling against simulated memory. These do not establish real-game timing.

Live checks used an unmodified upstream build at commit `065a94b2a4c55b5217ffd023d8736af21e2d6851`, with EU assets and isolated saves. The real Days AP client connected to a local seed server through the Lua mailbox, received 285 inventory entries, and acknowledged its starting mission 64 and Axel settings. Separate live grants verified potions, five slot rows and three Fire panels. A fresh Story start reached day 357. The Story camp's Normal Missions screen showed only Day 225 and mission 64 for that seed; unlocking and relocking mission 1 changed the already-open day list between two rows and one. The cache is rebuilt in its existing allocation, with its cursor and scroll state updated; no native callbacks or hooks are required. Normal menu confirmation entered mission 64 in Rocky Expanse with Axel. During that mission, Defensive Block Pack granted exactly one of each of its three items and reconnect preserved those counts, with no client task errors. A burst of 40 inventory queries was acknowledged without another Lua budget pause.

Addresses are checked against Yokimitsuro/khdays-decomp's EU YKGP target, independently of the experimental native checkout:

- `config/arm9/symbols.txt`: game state, mission ID, mission record, result record, scene record and session table.
- `src/engine/Scene_AdvanceToPending.c`: scene-record layout.
- `src/engine/Slot4_GetIfOccupied.c` and `data/main_worlds_02042958.c`: session-table layout.
- `src/overlays/scenes/ov002_field/Ov002_CreateAndRestoreHud.c`: mission member kind at +3.
- `src/overlays/scenes/ov002_field/Ov002_FillMissionResult.c`: result flags at +0x20.
- `src/overlays/screens/ov026_shop/Ov026_CanConfirmShopRow.c`: inventory counts at +0x810.
- `src/engine/GameState_GetField.c` and `BitArray_GetField.c`: game-state flag storage and the day field's bit order.
- `GameState_IsFlagSet.c` and `BitArray_TestBit.c`: flag 0x208c is bit 3 of game-state byte +0x422; flag 0x2087 is bit 0 of byte +0x423. `Ov044_ReloadSceneResources.c` uses the former for Xion, and `Ov002_FillMissionResult.c` tests the latter for withdrawal.
- `src/overlays/scenes/ov002_field/Ov002_StepSessionMenu.c`: the day-clock record's fields.
- `Ov002_GetMissionProgress.c` and `Ov002_Field_RequestTransfer.c`: field progress at +0x188/+0x18c/+0x190.
- `Ov002_SceneApplyPanelRequest.c`, `Ov002_MoveCursorTo.c` and `Ov002_ScenePanelIdleStep.c`: HUD options, cursor and count.
- `src/overlays/screens/ov025_camp_menu_2/Ov025_GetPageA.c`, `Ov025_PollPageInput.c`, `Ov025_InitObjectWithList.c`, `Ov025_QueryFieldBySelector.c` and `Ov025_BuildRecordNode.c`: menu context, list and record layout.
- `Ov025_GetPageB.c`, `Ov025_SetHandlerB.c`, `Ov025_ScrollList_BuildRows.c`, `Ov025_ScrollList_Open.c`, `Ov025_ScrollList_SelectRow.c`, `Ov025_ScrollList_SetupScrollBar.c` and `Ov025_ListViewUpdate.c`: the day-row allocation, names, count, cursor, scrolling and redraw flags. `Ov025_GetTableValue.c`, `Ov025_GetTableValueB.c` and overlay-25 symbols verify the day table at 0x020b39e4; `Ov025_GetVarRecordByIndex.c` verifies its name-record lookup.
- `Ov002_GetModuleSlot.c`, `Ov002_CreateTimedClass.c`, `Ov002_CreateEntryPool.c` and `Ov002_SpawnTimedElementAt.c`: chest pools and element layout. The overlay-2 symbols place `Ov002_Element_PickTick` at 0x0207a0c8.
- `src/overlays/system/ov107_enemy_common/Ov107_SetupActorManager.c`, `Ov107_FindMessageHandler.c`, `Ov107_AiState_LoadStats.c` and `src/engine/List_First.c`/`List_Next.c`: actor lists and stats.

The source connector's scan-reset bytes are retained as state tokens. They should not be described as a verified current-map API: the first is within the track record at 0x0204c3d8, and the other is the global byte set by `Ov002_SetGlobalByte1F.c`.

The 285 inventory keys and 91 mission records come from the current MelonMix connector working tree. They are data tables, not address authorities.

## Remaining runtime parity checks

- Manual and per-mission characters, flashback exceptions and Xion behavior.
- Enemy scaling and spawn/list changes.
- Chest vanilla-reward suppression and location reports.
- Mission reward suppression, result tracking and withdrawal handling.
- Final-mission gate and game completion.

The transferred implementation is 772 lines: 644 Lua lines, 85 Python bridge lines and 43 client additions, versus 1,549 lines in the current MelonMix connector (50.16% fewer). Fixtures and this documentation are counted separately. The gameplay fixture also checks withdrawal followed by a successful clear and the main frame callback's one-time ending report; the Python regression rejects inventory replies from a previous connection or query.

The source connector's badge probe has no gameplay effects, and its cutscene-skip experiment is not called by its frame loop; neither should be presented as working features.
