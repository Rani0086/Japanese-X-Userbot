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

@Client.on_message(filters.command(["mute", "unmute"], cmd) & filters.me)

async def mute(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    X = await edit_or_reply(message, "`Processing...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await X.edit("Ask Admin First")
    if not user_id:
        return await X.edit("User not found.")
    if user_id == client.me.id:
        return await X.edit("Where Can a Dog!.")
    if user_id in DEVS:
        return await X.edit("Can't Get Rid of Stupid Developers!")
    if user_id in (await list_admins(client, message.chat.id)):
        return await X.edit("I can't mute an admin, You know the rules, so do i.")
    mention = (await client.get_users(user_id)).mention
    msg = (
        f"**Muted User:** {mention}\n"
        f"**Muted By:** {message.from_user.mention if message.from_user else 'Anon'}\n"
    )
    if reason:
        msg += f"**Reason:** {reason}"
    await message.chat.restrict_member(user_id, permissions=ChatPermissions())
    await X.edit(msg)
