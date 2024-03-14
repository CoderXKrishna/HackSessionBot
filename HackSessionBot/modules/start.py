import re
from pyrogram import filters, StopPropagation
from pyrogram.types import CallbackQuery

from HackSessionBot import app, START_PIC
from HackSessionBot.Helpers.data import PM_TEXT, PM_BUTTON, HACK_MODS, HACK_TEXT

@app.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    user = message.from_user.mention
    bot = client.me.mention
    await message.reply_photo(
        photo=START_PIC,
        caption=PM_TEXT.format(user, bot),
        reply_markup=PM_BUTTON,
    )

@app.on_message(filters.command("hack") & filters.private)
async def hack_command(client, message):
    await message.reply_text(
        text=HACK_TEXT,
        reply_markup=HACK_MODS,
    )

@app.on_callback_query(filters.regex("hack_btn"))
async def hack_callback(client: app, query: CallbackQuery):
    await query.message.delete()
    await query.message.reply_text(
        text=HACK_TEXT,
        reply_markup=HACK_MODS,
    )
    query.answer("Hacking in progress...", show_alert=True)
    raise StopPropagation
