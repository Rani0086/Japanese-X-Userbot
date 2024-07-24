import html

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from JAPANESE.nxtgenhelper.basic import edit_or_reply
from JAPANESE.nxtgenhelper.parser import mention_html, mention_markdown
from .help import *

@Client.on_message(filters.command(["bots"], cmd) & filters.me)

async def get_list_bots(client: Client, message: Message):
    replyid = None
    if len(message.text.split()) >= 2:
        chat = message.text.split(None, 1)[1]
        grup = await client.get_chat(chat)
    else:
        chat = message.chat.id
        grup = await client.get_chat(chat)
    if message.reply_to_message:
        replyid = message.reply_to_message.id
    getbots = client.get_chat_members(chat)
    bots = []
    async for a in getbots:
        try:
            name = a.user.first_name + " " + a.user.last_name
        except:
            name = a.user.first_name
        if name is None:
            name = "☠️ 𝐃𝐞𝐥𝐞𝐭𝐞𝐝 𝐚𝐜𝐜𝐨𝐮𝐧𝐭"
        if a.user.is_bot:
            bots.append(mention_markdown(a.user.id, name))
    sakura = "**𝐀𝐥𝐥 𝐛𝐨𝐭𝐬 𝐢𝐧 𝐠𝐫𝐨𝐮𝐩 {}**\n".format(grup.title)
    sakura += "╒═══「 𝐁𝐨𝐭𝐬 」\n"
    for x in bots:
        sakura += "│ • {}\n".format(x)
    sakura += "╘══「 𝐓𝐨𝐭𝐚𝐥 {} 𝐁𝐨𝐭𝐬 」".format(len(bots))
    if replyid:
        await client.send_message(message.chat.id, sakura, reply_to_message_id=replyid)
    else:
        await message.edit(sakura)
