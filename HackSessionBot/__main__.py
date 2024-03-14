import asyncio
import importlib
from pyrogram import idle
from HackSessionBot import LOG, ALL_MODULES

async def start_bot():
    for all_module in ALL_MODULES:
        try:
            importlib.import_module(f"HackSessionBot.modules.{all_module}")
        except Exception as e:
            LOG.error(f"Error importing module {all_module}: {e}")
    LOG.print("[bold yellow]✨ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ")
    await idle() 
    LOG.print("[bold red]ᴄᴀɴᴄᴇʟɪɴɢ ᴀʟʟ ᴛᴀsᴋs.")

if __name__ == "__main__":
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        LOG.print("[bold red]ᴄᴀɴᴄᴇʟʟɪɴɢ ᴀʟʟ ᴛᴀsᴋs.")
