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

@Client.on_message(filters.command(["unban"], cmd) & filters.me)

async def member_unban(client: Client, message: Message):
    reply = message.reply_to_message
    X = await edit_or_reply(message, "`In progresss master...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await X.edit("Ask Admin First dude!")
    if reply and reply.sender_chat and reply.sender_chat != message.chat.id:
        return await X.edit("It's a channel, where can you ban it, okay?!")

    if len(message.command) == 2:
        user = message.text.split(None, 1)[1]
    elif len(message.command) == 1 and reply:
        user = message.reply_to_message.from_user.id
    else:
        return await X.edit(
            "Username where is the fool?!."
        )
    await message.chat.unban_member(user)
    umention = (await client.get_users(user)).mention
    await X.edit(f"Unbanned! {umention}")
