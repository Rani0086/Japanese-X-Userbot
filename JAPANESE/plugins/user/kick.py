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

@Client.on_message(filters.command(["kick"], cmd) & filters.me)

async def kick_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    X = await edit_or_reply(message, "`Processing...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await X.edit("I don't have enough permissions")
    if not user_id:
        return await X.edit("I can't find that user.")
    if user_id == client.me.id:
        return await X.edit("I can't kick myself.")
    if user_id == DEVS:
        return await X.edit("I can't kick my developer")
    if user_id in (await list_admins(client, message.chat.id)):
        return await X.edit("I can't kick an admin, You know the rules, so do i.")
    mention = (await client.get_users(user_id)).mention
    msg = f"""
**Kicked User:** {mention}
**Kicked By:** {message.from_user.mention if message.from_user else 'Anon'}"""
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if reason:
        msg += f"\n**Reason:** `{reason}`"
    try:
        await message.chat.ban_member(user_id)
        await X.edit(msg)
        await asyncio.sleep(1)
        await message.chat.unban_member(user_id)
    except ChatAdminRequired:
        return await X.edit("**Sorry You are not an admin**")
