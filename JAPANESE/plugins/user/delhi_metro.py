from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from JAPANESE.nxtgenhelper.basic import edit_or_reply
from JAPANESE.nxtgenhelper.PyroHelpers import ReplyCheck

from .help import *

# Delhi Metro Lines and Stations Information
delhi_metro_info = """
**Delhi Metro Lines and Stations Information:**

- **Line 1 (Red Line): Dilshad Garden to Rithala**
  - Dilshad Garden
  - Shahdara
  - Seelampur
  - Jama Masjid
  - Chawri Bazar
  - Rajeev Chowk
  - Rithala

- **Line 2 (Yellow Line): Jahangirpuri to HUDA City Centre**
  - Jahangirpuri
  - Samaypur Badli
  - Rohini Sector 18
  - Rohini Sector 19
  - Pitampura
  - Netaji Subhash Place
  - Keshav Puram
  - Kanhiya Nagar
  - Shahdara
  - JLN Stadium
  - Central Secretariat
  - Hauz Khas
  - Malviya Nagar
  - Saket
  - Qutab Minar
  - HUDA City Centre

- **Line 3 (Blue Line): Dwarka Sector 21 to NOIDA City Centre/Vaishali**
  - Dwarka Sector 21
  - Dwarka Sector 8
  - Janakpuri West
  - Kirti Nagar
  - Mandi House
  - Rajiv Chowk
  - Barakhamba Road
  - Patel Chowk
  - Chandni Chowk
  - Daryaganj
  - NOIDA City Centre
  - Vaishali

- **Line 4 (Blue Line Extension): Yamuna Bank to Vaishali**
  - Yamuna Bank
  - Anand Vihar
  - Vaishali

- **Line 5 (Yellow Line Extension): Mundka to Inderlok**
  - Mundka
  - Udyog Nagar
  - Inderlok

- **Line 6 (Violet Line): Kashmere Gate to Badarpur**
  - Kashmere Gate
  - Mandi House
  - Sarai Rohilla
  - Badarpur

- **Line 7 (Pink Line): Dwarka Sector 21 to Lajpat Nagar**
  - Dwarka Sector 21
  - Janakpuri West
  - Kirti Nagar
  - Rajendra Place
  - Pusa Institute
  - Karol Bagh
  - Lajpat Nagar

- **Line 8 (Magenta Line): Janakpuri West to Majlis Park**
  - Janakpuri West
  - R K Ashram Marg
  - Majlis Park

- **Line 9 (Aqua Line): Botanical Garden to NOIDA City Centre**
  - Botanical Garden
  - NOIDA City Centre

- **Line 10 (Red Line Extension): NOIDA City Centre to Sector 62**
  - NOIDA City Centre
  - Sector 62
"""

@Client.on_message(filters.command(["metro"], cmd) & filters.me)
def send_metro_info(client, message):
    message.reply_text(delhi_metro_info, parse_mode="markdown")


add_command_help(
    "•─╼⃝𖠁 Dᴇʟʜɪ Mᴇᴛʀᴏ",
    [
        ["metro <ʀᴇᴘʟʏ>", "Dᴇʟʜɪ Mᴇᴛʀᴏ ʟɪɴᴇs ᴀɴᴅ sᴛᴀᴛɪᴏɴs ɪɴғᴏʀᴍᴀᴛɪᴏɴ."],
    ],
) 
