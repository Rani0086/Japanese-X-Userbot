import aiohttp
from pyrogram import filters, Client
from pyrogram.types import Message
from config import CMD_HANDLER
from JAPANESE.nxtgenhelper.PyroHelpers import GetChatID, ReplyCheck
from .help import * 



@Client.on_message(filters.command(["genshin"], cmd) & filters.me)
