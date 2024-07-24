import html

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from JAPANESE.nxtgenhelper.basic import edit_or_reply
from JAPANESE.nxtgenhelper.parser import mention_html, mention_markdown
from .help import *

@Client.on_message(filters.command(["tagall"], cmd) & filters.me)

async def tag_all_users(client: Client, message: Message):
    await message.delete()
    if len(message.text.split()) >= 2:
        text = message.text.split(None, 1)[1]
    else:
        text = "𝐇𝐞𝐥𝐥𝐨 𝐉𝐀𝐏𝐀𝐍𝐄𝐒𝐄 𝐒𝐀𝐌𝐔𝐑𝐀𝐈'𝐒 😊"
    nobi = client.get_chat_members(message.chat.id)
    async for a in nobi:
        if not a.user.is_bot:
            text += mention_html(a.user.id, "\u200b")
    if message.reply_to_message:
        await client.send_message(
            message.chat.id,
            text,
            reply_to_message_id=message.reply_to_message.id,
            parse_mode=enums.ParseMode.HTML,
        )
    else:
        await client.send_message(
            message.chat.id, text, parse_mode=enums.ParseMode.HTML
        )
