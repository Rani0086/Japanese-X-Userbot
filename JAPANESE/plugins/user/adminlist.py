import html

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from JAPANESE.nxtgenhelper.basic import edit_or_reply
from JAPANESE.nxtgenhelper.parser import mention_html, mention_markdown
from .help import *

@Client.on_message(filters.command(["admins"], cmd) & filters.me)
async def adminlist(client: Client, message: Message):
    # Determine the chat to query
    if len(message.text.split()) >= 2:
        chat = message.text.split(None, 1)[1]
    else:
        chat = message.chat.id
    
    # Fetch chat information
    grup = await client.get_chat(chat)
    
    # Determine reply ID if message is a reply
    replyid = message.reply_to_message.id if message.reply_to_message else None
    
    # Initialize lists to store admins
    creator = []
    admin = []
    badmin = []
    
    # Iterate through chat members
    async for member in client.iter_chat_members(
        message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS
    ):
        name = member.user.first_name + (" " + member.user.last_name if member.user.last_name else "")
        if not name.strip():  # Handle missing names
            name = "☠️ 𝐃𝐞𝐥𝐞𝐭𝐞𝐝 𝐚𝐜𝐜𝐨𝐮𝐧𝐭"
        
        # Categorize members based on status
        if member.status == enums.ChatMemberStatus.ADMINISTRATOR:
            if member.user.is_bot:
                badmin.append(mention_markdown(member.user.id, name))
            else:
                admin.append(mention_markdown(member.user.id, name))
        elif member.status == enums.ChatMemberStatus.OWNER:
            creator.append(mention_markdown(member.user.id, name))
    
    # Sort admin lists alphabetically
    creator.sort()
    admin.sort()
    badmin.sort()
    
    # Prepare the message content
    sakura = "**Admins in {}**\n".format(grup.title)
    sakura += "╒═══「 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 」\n"
    
    # Function to send message if it exceeds length
    async def send_if_toolong():
        nonlocal sakura
        if len(sakura) >= 4096:
            if toolong:
                await message.reply(message.chat.id, sakura, reply_to_message_id=replyid)
            else:
                await message.edit(sakura)
            sakura = ""
    
    # Append creators to message
    for x in creator:
        sakura += "│ • {}\n".format(x)
        await send_if_toolong()
    
    # Append regular admins to message
    sakura += "╞══「 {} 𝐇𝐮𝐦𝐚𝐧 𝐀𝐝𝐦𝐢𝐧𝐢𝐬𝐭𝐫𝐚𝐭𝐨𝐫 」\n".format(len(admin))
    for x in admin:
        sakura += "│ • {}\n".format(x)
        await send_if_toolong()
    
    # Append bot admins to message
    sakura += "╞══「 {} 𝐁𝐨𝐭 𝐀𝐝𝐦𝐢𝐧𝐢𝐬𝐭𝐫𝐚𝐭𝐨𝐫 」\n".format(len(badmin))
    for x in badmin:
        sakura += "│ • {}\n".format(x)
        await send_if_toolong()
    
    # Append total admin count
    sakura += "╘══「 𝐓𝐨𝐭𝐚𝐥 {} 𝐀𝐝𝐦𝐢𝐧𝐬 」".format(len(creator) + len(admin) + len(badmin))
    
    # Send or edit message based on length
    if toolong:
        await message.reply(message.chat.id, sakura, reply_to_message_id=replyid)
    else:
        await message.edit(sakura)
        
