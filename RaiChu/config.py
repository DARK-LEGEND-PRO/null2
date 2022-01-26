## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQANH5SotQD33FHVGHMikCBdKMgqjzIDEt3yDct4_WtCQdOS1ZOtxQiZanEIFsMc6jJlvEIP2jbY0bK3zmdT5qbr2_TdsFfeFFIzSCY9YIPdzfwgJEqn7p-Io8Kl3cHXhRQBT1han1YnWDANU-NGLf_2JtHo6ALJKU8xc_HB_beuaM1RTJk5s34kpCZbjyhhsWtOW_41qWgglHxl5XHIb-Fil4G4FnaV-LwGN0a1YMucMnRdHl3_pEflB3NgoqZ7cH4FHRJ0O43kDr3PiepYJNvKa9SP_PzeYlIWNHFJb_jXk27Lfs_xk1SdR7LBAZ3HSdtAJcgsnJ3FZXInDy44_CS2AAAAATeg_ZoA")
BOT_TOKEN = getenv("BOT_TOKEN", "2100234484:AAEb0S-CWC4h2Xr1rOUft9PvbqPKszSnCxQ")
BOT_NAME = getenv("BOT_NAME", "Shubhanshu")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "Shubhanshu")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Shubhanshu")
ALIVE_NAME = getenv("ALIVE_NAME", "Levina")
BOT_USERNAME = getenv("BOT_USERNAME", "veezvideobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Shadow_Helper_1")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "VeezSupportGroup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "levinachannel")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1920507972").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")

