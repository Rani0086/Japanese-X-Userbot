from pyrogram import Client, filters
from pyrogram.types import Message
import instaloader
from config import CMD_HANDLER
from JAPANESE.nxtgenhelper.basic import edit_or_reply
from JAPANESE.nxtgenhelper.PyroHelpers import ReplyCheck

from .help import *



# Create an Instaloader instance
loader = instaloader.Instaloader()

@Client.on_message(filters.command(["instagram"], cmd) & filters.me)
def get_instagram_data(client, message: Message):
    if len(message.command) < 2:
        message.reply_text("Please provide an Instagram username. Usage: .instagram <username>")
        return

    username = message.command[1]
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        info = (
            f"**Username:** {profile.username}\n"
            f"**Full Name:** {profile.full_name}\n"
            f"**Bio:** {profile.biography}\n"
            f"**Followers:** {profile.followers}\n"
            f"**Following:** {profile.followees}\n"
            f"**Posts:** {profile.mediacount}"
        )
        message.reply_text(info, parse_mode="markdown")
    except Exception as e:
        message.reply_text(f"An error occurred: {e}")
        
add_command_help(
    "•─╼⃝𖠁 Iɴsᴛᴀɢʀᴀᴍ",
    [
        ["instagram <ʀᴇᴘʟʏ>", "Tᴏ ᴄʜᴇᴄᴋ Iɴsᴛᴀɢʀᴀᴍ ᴜsᴇʀ ᴘᴏsᴛ ғᴏʟʟᴏᴡɪɴɢ ғᴏʟʟᴏᴡᴇʀs ʙɪᴏғᴜʟʟ ɴᴀᴍᴇ ᴜsᴇʀɴᴀᴍᴇ."],
    ],
) 
