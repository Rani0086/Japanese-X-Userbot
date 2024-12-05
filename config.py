import os
from distutils.util import strtobool
from os import getenv
from JAPANESE.nxtgenhelper.cmd import cmd
from dotenv import load_dotenv

load_dotenv("config.env")

ALIVE_TEXT = getenv("ALIVE_TEXT", "✧✧ niyoto userbot  ✧✧")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://envs.sh/AIr.jpg")
API_HASH = getenv("API_HASH", "009e3d8c1bdc89d5387cdd8fd182ec15")
API_ID = getenv("API_ID", "23255238")
BOT_VER = "5.0.0@main"
BRANCH = getenv("BRANCH", "main") #don't change this line 
CMD_HNDLR = cmd
BOT_TOKEN = getenv("BOT_TOKEN", "none")
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "")
CHANNEL = getenv("CHANNEL", "niyoto_supoort")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
GIT_TOKEN = getenv("GIT_TOKEN", "")
GROUP = getenv("GROUP", "waifexanime")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
REPO_URL = getenv("REPO_URL", "https://github.com/Team-Japanese/Japanese-X-Userbot")
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
