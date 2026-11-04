import asyncio
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from CommonClient import CommonContext ,server_loop
from kvui import GameManager
from worlds.khdays.client.DaysUI import DaysUI
from worlds.khdays.client.commandHistory import DaysContext
from worlds.khdays import KHDaysWorld

async def main():
    ctx = DaysContext(None,None)
    ctx.server_task = asyncio.create_task(server_loop(ctx))

    ctx.game = "KH Days"
    
    ui = DaysUI(ctx)
    ctx.ui = ui
    ui.base_title = "Days Client"
    await ui.async_run(async_lib="asyncio")

    await ctx.shutdown()

asyncio.run(main())
