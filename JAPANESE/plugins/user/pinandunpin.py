import asyncio

from pyrogram import Client, filters
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, ChatPrivileges, Message


from config import CMD_HANDLER
from JAPANESE.nxtgenhelper.adminHelpers import DEVS
from JAPANESE.nxtgenhelper.basic import edit_or_reply
from .help import *
from JAPANESE.utils.misc import extract_user, extract_user_and_reason, list_admins

unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)

@Client.on_message(filters.command(["pin", "unpin"], cmd) & filters.me)

async def pin_message(client: Client, message: Message):
    if not message.reply_to_message:
        return await edit_or_reply(message, "Reply to a message to pin/unpin it.")
    
    edit_msg = await edit_or_reply(message, "`Processing...`")
    
    # Check bot's permissions to pin messages
    bot = await client.get_chat_member(message.chat.id, client.me.id)
    if not bot.can_pin_messages:
        return await edit_msg.edit("Sorry, I don't have permission to pin messages.")
    
    replied_message = message.reply_to_message
    if message.command and message.command[0][0] == "u":
        await replied_message.unpin()
        return await edit_msg.edit(
            f"**Unpinned [this]({replied_message.link}) message.**",
            disable_web_page_preview=True,
        )
    
    await replied_message.pin(disable_notification=True)
    await edit_msg.edit(
        f"**Pinned [this]({replied_message.link}) message.**",
        disable_web_page_preview=True,
    )
