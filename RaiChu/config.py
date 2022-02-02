## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQBHX8fYTkMCCu-IyMMNzw-CgU3Uo8ITsxcc0Z5xNOXrNfjD7vuXOCe5h6SxSpMdVC4YgQps8rNNvf8efxuq5qzDvGRLEg3cM0Hv7vWFDY4oDipXx4IGQyfHflVxqk30QcJYGynE4kJw8PAmXHP_q5cRkFdC_5wl6qR_UyWqLUueAuOEAQz-VPRERbgRCYVCIaUtwn_rWEdRDpotkEhnihjD7Cu7LCTNQb7cyVbIFYyiGzYvBapNM7YZaLPc5H-oOpqpCUNDMzrjRKFYtDdXnTQcmHX0Zc2dWl-DMrJRjt1ZXBnjWTOhfBJ5k93UBeLbLoMWXpa32Yj4LHObGmi59JMqAAAAAS-7dKkA")
BOT_TOKEN = getenv("BOT_TOKEN", "5173319885:AAFP6amIZWbmcjhpVzlJGt4Ybr5VN-6ecWU")
BOT_NAME = getenv("BOT_NAME", "Nrx")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "Zaid")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Timesisnotwaiting")
ALIVE_NAME = getenv("ALIVE_NAME", "Yumi")
BOT_USERNAME = getenv("BOT_USERNAME", "DraMic_MusicBoT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "IYi_Sher_Vc")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "friends_chat_international_group")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "levinachannel")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")

