import os
import asyncio
import logging
from config import Config
from pyrogram import Client
from rich.console import Console
from rich.table import Table
from HackSessionBot.Helpers.data import LOG_TEXT, ART
from pyromod import listen

# getting variables
API_ID = Config.API_ID
API_HASH = Config.API_HASH
TOKEN = Config.TOKEN
START_PIC = Config.START_PIC
CHAT = Config.CHAT

if not API_ID or not API_HASH or not TOKEN:
    raise Exception("Missing required variables in config.py")

# rich
LOG = Console()

# logger
logging.basicConfig(level=logging.INFO)

# client
app = Client(
    "SupremeStark",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN
)

# check if the bot is already running
if not app.bot_token:
    raise Exception("Bot token not found. Make sure you have added it to config.py")


async def HackSessionBot():
    os.system("clear")
    header = Table(show_header=True, header_style="bold green")
    header.add_column(LOG_TEXT)
    LOG.print(header)
    LOG.print(f"[bold cyan]{ART}")
    LOG.print("[bold yellow]sᴛᴀʀᴛɪɴɢ ʏᴏᴜʀ ʙᴏᴛ ɴᴏᴡ.......")
    try:
        await app.start()
    except Exception as e:
        LOG.print(f"[bold red]Error starting the bot: {e}")


async def graceful_stop():
    await app.stop()
    LOG.print("[bold green]Bot stopped gracefully")


loop = asyncio.get_event_loop()
loop.run_
