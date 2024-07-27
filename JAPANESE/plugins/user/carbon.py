import asyncio
from io import BytesIO

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from JAPANESE import aiosession
from JAPANESE.nxtgenhelper.basic import edit_or_reply
from JAPANESE.nxtgenhelper.PyroHelpers import ReplyCheck

from .help import *


async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@Client.on_message(filters.command(["carbon"], cmd) & filters.me)
async def carbon_func(client: Client, message: Message):
    # Determine the text to be processed
    if len(message.command) == 1:
        text = None
    else:
        text = message.text.split(None, 1)[1]

    # If there's no text, try to use text from the replied message
    if not text and message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption

    # If no text is found, delete the message and exit
    if not text:
        await message.delete()
        return

    # Notify the user that the processing is starting
    progress_msg = await edit_or_reply(message, "`Preparing Carbon . . .`")
    
    # Create the Carbon image
    carbon = await make_carbon(text)
    
    # Update the message to indicate uploading is in progress
    await progress_msg.edit("`Uploading . . .`")
    
    # Upload the Carbon image and clean up
    await asyncio.gather(
        progress_msg.delete(),
        client.send_photo(
            message.chat.id,
            carbon,
            caption=f"**Carbonised by** {client.me.mention}",
            reply_to_message_id=ReplyCheck(message),
        ),
    )
    
    # Close the Carbon file
    carbon.close()
    


add_command_help(
    "•─╼⃝𖠁 ᴄᴀʀʙᴏɴ",
    [
        ["carbon <ʀᴇᴘʟʏ>", "Tᴇxᴛ ᴄᴀʀʙᴏɴɪᴢᴀᴛɪᴏɴ ᴡɪᴛʜ ᴅᴇғᴀᴜʟᴛ ꜱᴇᴛᴛɪɴɢꜱ."],
    ],
) 
