## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "Umk")
API_ID = int(getenv("API_ID", "7200977"))
API_HASH = getenv("API_HASH", "bdf80270f92cf659aedb1eeccf8320ab")
OWNER_NAME = getenv("OWNER_NAME", "Adrish")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Adrish_Owner")
ALIVE_NAME = getenv("ALIVE_NAME", "Adrish")
BOT_USERNAME = getenv("BOT_USERNAME", "Adrish2music_Bot")
OWNER_ID = getenv("OWNER_ID", "5131191131")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Adrish2Music")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Adrish_Support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Adrish_Network")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5131191131").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/7ad914c623584a5de931d.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/89f61752491abcd14829f.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TeamAdrish/AdrishVCplayer")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/6d1534eb89423d381236d.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/671fd52ee783558a0ef4a.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/a758a07362d24f095252a.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/6153a992bd8bed9be5827.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/6ef36393ab3b404dbd819.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/6ef36393ab3b404dbd819.jpg")
