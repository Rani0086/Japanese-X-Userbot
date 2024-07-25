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
    edit_msg = await edit_or_reply(message, "`Processing...`")
    
    # Check bot's permissions to restrict members
    bot = await client.get_chat_member(message.chat.id, client.me.id)
    if not bot.can_restrict_members:
        return await edit_msg.edit("Sorry, I don't have permission to unban members.")
    
    # Check if replying to a message and that message is from a channel
    if reply and reply.sender_chat and reply.sender_chat.type == 'channel':
        return await edit_msg.edit("Cannot unban members from a channel.")
    
    # Determine user ID to unban
    if len(message.command) == 2:
        user = message.text.split(None, 1)[1]
    elif len(message.command) == 1 and reply:
        user = reply.from_user.id
    else:
        return await edit_msg.edit("Provide a valid username or reply to a message to unban.")

    try:
        # Unban the member
        await message.chat.unban_member(user)
        
        # Get user mention for the unban message
        user_obj = await client.get_users(user)
        mention = user_obj.mention
        
        # Edit message to confirm unban
        await edit_msg.edit(f"Successfully unbanned {mention}")
    except Exception as e:
        await edit_msg.edit(f"Failed to unban user: {str(e)}")
