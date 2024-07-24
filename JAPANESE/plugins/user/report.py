import html

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from JAPANESE.nxtgenhelper.basic import edit_or_reply
from JAPANESE.nxtgenhelper.parser import mention_html, mention_markdown
from .help import *

@Client.on_message(filters.command(["report"], cmd) & filters.me)

async def report_admin(client: Client, message: Message):
    await message.delete()

    # Extract the report text if provided
    if len(message.text.split()) >= 2:
        text = message.text.split(None, 1)[1]
    else:
        text = None

    # Get chat info
    grup = await client.get_chat(message.chat.id)

    # Collect all non-bot administrators
    admin = []
    async for a in client.iter_chat_members(
        message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS
    ):
        if not a.user.is_bot:
            admin.append(mention_html(a.user.id, "\u200b"))

    # Determine the message content based on conditions
    if message.reply_to_message:
        if text:
            sakura = html.escape(text)
        else:
            sakura = "{} reported to admins.".format(
                mention_html(
                    message.reply_to_message.from_user.id,
                    message.reply_to_message.from_user.first_name,
                )
            )
    else:
        if text:
            sakura = html.escape(text)
        else:
            sakura = f"Calling admins in {grup.title}."

    # Add admin mentions to the message content
    sakura += "".join(admin)

    # Send the message
    if message.reply_to_message:
        await client.send_message(
            message.chat.id,
            sakura,
            reply_to_message_id=message.reply_to_message.id,
            parse_mode=enums.ParseMode.HTML,
        )
    else:
        await client.send_message(
            message.chat.id, sakura, parse_mode=enums.ParseMode.HTML
                                          )
        
