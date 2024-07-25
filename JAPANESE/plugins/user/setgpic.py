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

@Client.on_message(filters.command(["setgcpic"], cmd) & filters.me)
async def set_chat_photo(client: Client, message: Message):
    chat_member = await client.get_chat_member(message.chat.id, client.me.id)
    can_change_info = chat_member.can_change_info
    can_change_member = message.chat.permissions.can_change_info

    if not (can_change_info or can_change_member):
        await message.edit_text("You don't have enough permissions.")
        return

    if message.reply_to_message and message.reply_to_message.photo:
        await client.set_chat_photo(message.chat.id, photo=message.reply_to_message.photo.file_id)
    else:
        await message.edit_text("Reply to a photo to set it!")

