import logging
from typing import List, Dict, Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

class HackBot:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.pm_text = self.generate_pm_text()
        self.hack_text = self.generate_hack_text()
        self.pm_button = self.generate_pm_button()
        self.hack_mods = self.generate_hack_mods()
        self.log_text = self.generate_log_text()
        self.art = self.generate_art()

    @property
    def name(self) -> str:
        return "HackBot"

    @property
    def id(self) -> str:
        return "123456789"

    @property
    def phone_number(self) -> str:
        return "+1234567890"

    @property
    def username(self) -> str:
        return "@hackbot"

    def generate_pm_text(self) -> str:
        return f"**ʜᴇʏ {self.name} (<code>{self.id}</code>),**\nɪ'ᴍ **{self.name}** ᴀ ʙᴏᴛ ᴛᴏ ʜᴀᴄᴋ ᴜsᴇʀs ᴀᴄᴄᴏᴜɴᴛ.\n\nɪ  sᴜᴘᴘᴏʀᴛ ʙᴏᴛʜ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ\nᴄʟɪᴄᴋ ᴏɴ ʜᴀᴄᴋ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴡʜᴀᴛ ɪ ᴄᴀɴ ᴅᴏ."

    def generate_hack_text(self) -> str:
        return f"'A' :~ [ᴄʜᴇᴄᴋ ᴜsᴇʀ ᴏᴡɴ ɢʀᴏᴜᴘs ᴀɴᴅ ᴄʜᴀɴɴᴇʟs]\n'B' :~ [ᴄʜᴇᴄᴋ ᴜsᴇʀ ᴀʟʟ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ʟɪᴋᴇ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ, ᴜsʀɴᴀᴍᴇ... ᴇᴛᴄ]\n'C' :~ [ʙᴀɴ ᴀ ɢʀᴏᴜᴘ {ɢɪᴠᴇ ᴍᴇ Sᴛʀɪɴɢsᴇssɪᴏɴ ᴀɴᴅ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ɪ ᴡɪʟʟ ʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ᴛʜᴇʀᴇ}]\n'D' :~ [ᴋɴᴏᴡ ᴜsᴇʀ ʟᴀsᴛ ᴏᴛᴘ {𝟷sᴛ ᴜsᴇ ᴏᴘᴛɪᴏɴ B ᴛᴀᴋᴇ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴀɴᴅ ʟᴏɢɪɴ ᴛʜᴇʀᴇ Aᴄᴄᴏᴜɴᴛ ᴛʜᴇɴ ᴜsᴇ ᴍᴇ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴏᴛᴘ}]\n'E' :~ [Jᴏɪɴ A Gʀᴏᴜᴘ/Cʜᴀɴɴᴇʟ ᴠɪᴀ Sᴛʀɪɴɢsᴇssɪᴏɴ]\n'F' :~ [Lᴇᴀᴠᴇ A Gʀᴏᴜᴘ/Cʜᴀɴɴᴇʟ ᴠɪᴀ Sᴛʀɪɴɢsᴇssɪᴏɴ]\n'G' :~ [Dᴇʟᴇᴛᴇ A Gʀᴏᴜᴘ/Cʜᴀɴɴᴇʟ]\n'H' :~ [ᴄʜᴇᴄᴋ ᴜsᴇʀ ᴛᴡᴏ sᴛᴇᴘ ɪs ᴇɴᴇᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ]\n'I' :~ [ᴛᴇʀᴍɪɴᴀᴛᴇ Aʟʟ ᴄᴜʀʀᴇɴᴛ ᴀᴄᴛɪᴠᴇ sᴇssɪᴏɴs ᴇxᴄᴇᴘᴛ Yᴏᴜʀ Sᴛʀɪɴɢsᴇssɪᴏɴ]\n'J' :~ [ᴅᴇʟᴇᴛᴇ Aᴄᴄᴏᴜɴᴛ]\n'K' :~ 
