import html

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from JAPANESE.nxtgenhelper.basic import edit_or_reply
from JAPANESE.nxtgenhelper.parser import mention_html, mention_markdown
from .help import *

@Client.on_message(filters.command(["admins"], cmd) & filters.me)
async def adminlist(client: Client, message: Message):
    replyid = None
    toolong = False
    if len(message.text.split()) >= 2:
        chat = message.text.split(None, 1)[1]
        grup = await client.get_chat(chat)
    else:
        chat = message.chat.id
        grup = await client.get_chat(chat)
    if message.reply_to_message:
        replyid = message.reply_to_message.id
    creator = []
    admin = []
    badmin = []
    async for a in client.get_chat_members(
        message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS
    ):
        try:
            name = a.user.first_name + " " + a.user.last_name
        except:
            name = a.user.first_name
        if name is None:
            name = "☠️ 𝐃𝐞𝐥𝐞𝐭𝐞𝐝 𝐚𝐜𝐜𝐨𝐮𝐧𝐭"
        if a.status == enums.ChatMemberStatus.ADMINISTRATOR:
            if a.user.is_bot:
                badmin.append(mention_markdown(a.user.id, name))
            else:
                admin.append(mention_markdown(a.user.id, name))
        elif a.status == enums.ChatMemberStatus.OWNER:
            creator.append(mention_markdown(a.user.id, name))
    admin.sort()
    badmin.sort()
    totaladmins = len(creator) + len(admin) + len(badmin)
    sakura = "**Admins in {}**\n".format(grup.title)
    sakura += "╒═══「 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 」\n"
    for x in creator:
        sakura += "│ • {}\n".format(x)
        if len(sakura) >= 4096:
            await message.reply(message.chat.id, sakura, reply_to_message_id=replyid)
            sakura = ""
            toolong = True
    sakura += "╞══「 {} 𝐇𝐮𝐦𝐚𝐧 𝐀𝐝𝐦𝐢𝐧𝐢𝐬𝐭𝐫𝐚𝐭𝐨𝐫 」\n".format(len(admin))
    for x in admin:
        sakura += "│ • {}\n".format(x)
        if len(sakura) >= 4096:
            await message.reply(message.chat.id, sakura, reply_to_message_id=replyid)
            sakura = ""
            toolong = True
    sakura += "╞══「 {} 𝐁𝐨𝐭 𝐀𝐝𝐦𝐢𝐧𝐢𝐬𝐭𝐫𝐚𝐭𝐨𝐫 」\n".format(len(badmin))
    for x in badmin:
        sakura += "│ • {}\n".format(x)
        if len(sakura) >= 4096:
            await message.reply(message.chat.id, sakura, reply_to_message_id=replyid)
            sakura = ""
            toolong = True
    sakura += "╘══「 𝐓𝐨𝐭𝐚𝐥 {} 𝐀𝐝𝐦𝐢𝐧𝐬 」".format(totaladmins)
    if toolong:
        await message.reply(message.chat.id, sakura, reply_to_message_id=replyid)
    else:
        await message.edit(sakura)
