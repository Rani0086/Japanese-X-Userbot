#MIT License


#Copyright (c) 2024 Japanese-X-Userbot

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


import random
from pyrogram import Client, filters
from config import SUDO_USERS

from .help import * 


@Client.on_message(
    filters.command(["mangalist"], ".") & (filters.me | filters.user(SUDO_USERS))
)


manga_titles = [
    "Naruto",
    "One Piece",
    "Attack on Titan",
    "Dragon Ball",
    "My Hero Academia",
    "Death Note",
    "Fullmetal Alchemist",
    "Tokyo Ghoul",
    "Demon Slayer",
    "One Punch Man"
]

random_title = random.choice(manga_titles)
print(random_title)


add_command_help(
    "•─╼⃝𖠁 Mᴀɴɢᴀ ʟɪsᴛ",
    [
       ["mangalist", "Gɪᴠᴇ random Mᴀɴɢᴀ ʟɪsᴛ name."],
        ],
)
