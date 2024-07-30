from pyrogram import Client, filters
from google.oauth2 import service_account
from googleapiclient.discovery import build
import io
import os
from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from JAPANESE.nxtgenhelper.basic import edit_or_reply
from JAPANESE.nxtgenhelper.PyroHelpers import ReplyCheck

from .help import *


# Path to the credentials file
SERVICE_ACCOUNT_FILE = 'path/to/credentials.json'
SCOPES = ['https://www.googleapis.com/auth/drive']

# Authenticate and create the Google Drive API service
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
drive_service = build('drive', 'v3', credentials=credentials)

# Helper function to upload a file to Google Drive
def upload_to_drive(file_path, mime_type):
    file_metadata = {'name': os.path.basename(file_path)}
    media = io.BytesIO(open(file_path, 'rb').read())
    request = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    )
    file = request.execute()
    return file.get('id')

# Helper function to download a file from Google Drive
def download_from_drive(file_id, destination_path):
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.FileIO(destination_path, 'wb')
    downloader = googleapiclient.http.MediaIoBaseDownloader(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}%.")
    fh.close()

@Client.on_message(filters.command(["upload"], cmd) & filters.me)
async def upload_command(client, message):
    if message.reply_to_message and message.reply_to_message.document:
        file = message.reply_to_message.document
        file_path = await client.download_media(file.file_id, "temp_file")
        mime_type = file.mime_type or "application/octet-stream"
        file_id = upload_to_drive(file_path, mime_type)
        await message.reply(f"File uploaded successfully! [Drive File](https://drive.google.com/file/d/{file_id}/view)")
        os.remove(file_path)
    else:
        await message.reply("Please reply to a file with the .upload.")

@Client.on_message(filters.command(["download"], cmd) & filters.me)
async def download_command(client, message):
    if len(message.command) < 2:
        return await message.reply("Please provide the Google Drive file ID.")
    
    file_id = message.command[1]
    destination_path = "downloaded_file"
    download_from_drive(file_id, destination_path)
    await client.send_document(message.chat.id, destination_path)
    os.remove(destination_path)

add_command_help(
    "•─╼⃝𖠁 Gᴏᴏɢʟᴇ Dʀɪᴠᴇ",
    [
        ["upload <ʀᴇᴘʟʏ>", "Tᴏ ᴜᴘʟᴏᴀᴅ Gᴏᴏɢʟᴇ Dʀɪᴠᴇ ғɪʟᴇ."],
        ["download <ʀᴇᴘʟʏ>", "Tᴏ Dᴏᴡɴʟᴏᴀᴅ Gᴏᴏɢʟᴇ Dʀɪᴠᴇ ғɪʟᴇ."],
    ],
) 
