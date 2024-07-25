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

async def pin_message(client: Client, message):
    if not message.reply_to_message:
        return await edit_or_reply(message, "Reply to a message to pin/unpin it.")
    X = await edit_or_reply(message, "`Processing...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_pin_messages:
        return await X.edit("I don't have enough permissions")
    r = message.reply_to_message
    if message.command[0][0] == "u":
        await r.unpin()
        return await X.edit(
            f"**Unpinned [this]({r.link}) message.**",
            disable_web_page_preview=True,
        )
    await r.pin(disable_notification=True)
    await X.edit(
        f"**Pinned [this]({r.link}) message.**",
        disable_web_page_preview=True,
    )
