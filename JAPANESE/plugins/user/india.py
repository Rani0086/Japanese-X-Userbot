from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from JAPANESE.nxtgenhelper.basic import edit_or_reply
from JAPANESE.nxtgenhelper.PyroHelpers import ReplyCheck

from .help import *


# Information about Indian states and major cities
india_states_info = """
**Indian States and Major Cities:**

- **Andhra Pradesh**
  - Major Cities: Visakhapatnam, Vijayawada, Tirupati, Guntur

- **Arunachal Pradesh**
  - Major Cities: Itanagar, Tawang, Pasighat, Ziro

- **Assam**
  - Major Cities: Guwahati, Dispur, Silchar, Jorhat

- **Bihar**
  - Major Cities: Patna, Gaya, Bhagalpur, Muzaffarpur

- **Chhattisgarh**
  - Major Cities: Raipur, Bilaspur, Korba, Durg

- **Goa**
  - Major Cities: Panaji, Vasco da Gama, Margao, Mapusa

- **Gujarat**
  - Major Cities: Ahmedabad, Surat, Vadodara, Rajkot

- **Haryana**
  - Major Cities: Chandigarh, Faridabad, Gurgaon, Ambala

- **Himachal Pradesh**
  - Major Cities: Shimla, Manali, Dharamshala, Kullu

- **Jharkhand**
  - Major Cities: Ranchi, Jamshedpur, Dhanbad, Bokaro

- **Karnataka**
  - Major Cities: Bangalore, Mysore, Hubli-Dharwad, Mangalore

- **Kerala**
  - Major Cities: Thiruvananthapuram, Kochi, Kozhikode, Kannur

- **Madhya Pradesh**
  - Major Cities: Bhopal, Indore, Jabalpur, Gwalior

- **Maharashtra**
  - Major Cities: Mumbai, Pune, Nagpur, Nashik

- **Manipur**
  - Major Cities: Imphal, Thoubal, Churachandpur, Ukhrul

- **Meghalaya**
  - Major Cities: Shillong, Tura, Jowai, Nongstoin

- **Mizoram**
  - Major Cities: Aizawl, Lunglei, Champhai, Kolasib

- **Nagaland**
  - Major Cities: Kohima, Dimapur, Mokokchung, Tuensang

- **Odisha**
  - Major Cities: Bhubaneswar, Cuttack, Rourkela, Berhampur

- **Punjab**
  - Major Cities: Chandigarh, Amritsar, Ludhiana, Jalandhar

- **Rajasthan**
  - Major Cities: Jaipur, Udaipur, Jodhpur, Kota

- **Sikkim**
  - Major Cities: Gangtok, Namchi, Pelling, Mangan

- **Tamil Nadu**
  - Major Cities: Chennai, Coimbatore, Madurai, Tiruchirappalli

- **Telangana**
  - Major Cities: Hyderabad, Warangal, Karimnagar, Nizamabad

- **Tripura**
  - Major Cities: Agartala, Udaipur, Kailashahar, Dharmanagar

- **Uttar Pradesh**
  - Major Cities: Lucknow, Kanpur, Agra, Varanasi

- **Uttarakhand**
  - Major Cities: Dehradun, Nainital, Haridwar, Roorkee

- **West Bengal**
  - Major Cities: Kolkata, Howrah, Siliguri, Durgapur
"""

@Client.on_message(filters.command(["india"], cmd) & filters.me)
def send_states_info(client, message):
    message.reply_text(india_states_info, parse_mode="markdown")



add_command_help(
    "•─╼⃝𖠁 Gᴏᴏɢʟᴇ Dʀɪᴠᴇ",
    [
        ["india", "Tᴏ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ Iɴᴅɪᴀ sᴛᴀᴛᴇ ᴀɴᴅ ᴄɪᴛʏ."],
    ],
) 

