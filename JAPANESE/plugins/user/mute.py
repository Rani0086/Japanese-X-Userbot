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

@Client.on_message(filters.command(["mute"], cmd) & filters.me)

async def mute(client: Client, message: Message):
    # Extract user_id and reason from the message
    user_id, reason = await extract_user_and_reason(message)
    
    # Initial response message
    X = await edit_or_reply(message, "`Processing...`")
    
    # Check if bot has the necessary permissions to restrict members
    bot_member = await client.get_chat_member(message.chat.id, client.me.id)
    if not bot_member.can_restrict_members:
        return await X.edit("Ask Admin First")

    # Check if user_id exists
    if not user_id:
        return await X.edit("User not found.")
    
    # Check if trying to mute itself
    if user_id == client.me.id:
        return await X.edit("Where Can a Dog!.")
    
    # Check if user_id is in the list of developers (DEVS)
    if user_id in DEVS:
        return await X.edit("Can't Get Rid of Stupid Developers!")
    
    # Check if user_id is an admin
    admins = await list_admins(client, message.chat.id)
    if user_id in admins:
        return await X.edit("I can't mute an admin, You know the rules, so do i.")
    
    # Fetch user mention for display
    user = await client.get_users(user_id)
    mention = user.mention
    
    # Construct the message to display
    msg = f"**Muted User:** {mention}\n"
    msg += f"**Muted By:** {message.from_user.mention if message.from_user else 'Anon'}\n"
    
    # Add reason if provided
    if reason:
        msg += f"**Reason:** {reason}"
    
    # Restrict user's permissions in the chat
    await message.chat.restrict_member(user_id, permissions=ChatPermissions())
    
    # Edit the response message with the final output
    await X.edit(msg)
    
