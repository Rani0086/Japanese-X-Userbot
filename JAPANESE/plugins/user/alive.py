import asyncio
import os
import time
from platform import python_version

from pyrogram import Client
from pyrogram import __version__ as versipyro
from pyrogram import filters
from pyrogram.types import Message

from config import BOT_VER, CHANNEL
from config import CMD_HANDLER
from config import GROUP, OWNER_ID
from JAPANESE import CMD_HELP, StartTime
from JAPANESE.nxtgenhelper.basic import edit_or_reply
from JAPANESE.nxtgenhelper.PyroHelpers import ReplyCheck
from JAPANESE.utils import get_readable_time
from JAPANESE.utils.misc import restart

from .help import *

modules = CMD_HELP
alivemodules = CMD_HELP

@Client.on_message(filters.command(["alive", "awake"], cmd) & filters.me)
async def alip(client: Client, message: Message):
    X = await edit_or_reply(message, "🌸")
    await asyncio.sleep(5)
    
    # Determine whether to send a video or photo based on the file extension
    send_func = client.send_video if alive_logo.endswith(".mp4") else client.send_photo
    
    # Calculate uptime in a readable format
    uptime = await get_readable_time((time.time() - StartTime))
    
    # Construct the message content
    nobi = (
        f"<b>{alive_text}</b>\n\n"
        f"<b>•─╼⃝ 𝐒ʏꜱᴛᴇ𝐌 𝐒ᴛᴀᴛᴜ𝐒 </b>\n\n"
        f"<b>𝐌ʏ 𝐌ᴀꜱᴛᴇ𝐑:</b> [{client.me.mention}](tg://user?id={OWNER_ID}) \n\n"
        f"<b>𝐏ʏʀᴏɢʀᴀ𝐌 𝐕ᴇʀꜱɪᴏ𝐍:</b> <code>{versipyro}</code>\n\n"
        f"<b>𝐁ᴏᴛ 𝐔ᴘᴛɪᴍ𝐄:</b> <code>{uptime}</code> \n\n"
        f"<b>𝐕ᴇʀꜱɪᴏ𝐍:</b> <code>{BOT_VER}</code> \n\n"
        f"<b>𝐌ᴏᴅᴜʟᴇ𝐒:</b> <code>{len(modules)} 𝐌ᴏᴅᴜʟᴇ𝐒</code> \n\n"
        f"<b>𝐏ʏᴛʜᴏ𝐍 𝐕ᴇʀꜱɪᴏ𝐍:</b> <code>{python_version()}</code> \n\n"
        f"<b>𝐆ʀᴏᴜ𝐏 :</b> [𝐒ᴜᴘᴘᴏʀ𝐓](https://t.me/Japanese_Userbot_Support)** \n\n"
        f"<b>𝐂ʜᴀɴɴᴇʟ:<b> [𝐔ᴘᴅᴀᴛᴇ𝐒](https://t.me/Japanese_Userbot)** \n\n"
        f"<b>[𝐃ᴇᴘʟᴏʏ](http://dashboard.heroku.com/new?template=https://github.com/Team-Japanese/Japanese-X-Userbot) 𝐘ᴏᴜʀ 𝐎𝐖ɴ [𝐉𝐀𝐏𝐀𝐍𝐄𝐒𝐄-𝐗-𝐔𝐒𝐄𝐑𝐁𝐎𝐓](http://github.com/Team-Japanese/Japanese-X-Userbot) ✧\n\n"
    )

    try:
        # Send the message with appropriate media type
        await send_func(
            message.chat.id,
            alive_logo,
            caption=nobi,
            reply_to_message_id=ReplyCheck(message),
        )
        await X.delete()
    except Exception as e:
        # If sending fails, edit X with the message content
        await X.edit(nobi, disable_web_page_preview=True)
        print(f"Exception occurred while sending alive message: {str(e)}")
        


add_command_help(
    "•─╼⃝𖠁 Aʟɪᴠᴇ",
    [
       ["alive", "Send alive text."],
    ],
  )
