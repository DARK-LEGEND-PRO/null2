## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQBW-CFTcF8C_UUYv-jDmOQGeb6a0OXJO20QQPNjcphBbxJ1n5ZMGLneBgbdRCMbcmrS2yTBNgiwYcUE0CfvH-mXnsM2M3g66vOQDt8CfoPY-qdPTe8mXpaFNmnSgVQ-dNIpngzxQBa_LdmDCXJleIXOTbnEU_7hfFENj8ZzzJh4lAe3Ksx7xPMvZIpmxT_UFVcukg0755YAm4ImARE58JLAnPaz7l5hdrZAxv39pT3J2FyZla2mwE9rXLEuHPJ7tC_eEBwz2e7dUh-97z5jKcrxqr7gLhahXqBjC-MSgelrvfzxUYE4z6__qJZWeEeOzKUbMCbrDRswXsdzrOVkIPJzdxQy8QA")
BOT_TOKEN = getenv("BOT_TOKEN", "5246681780:AAGOFHt8x71S2Xkpe3W2zepAVq9bKAJ0lvY")
BOT_NAME = getenv("BOT_NAME", "Nrx")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "Zaid")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Timesisnotwaiting")
ALIVE_NAME = getenv("ALIVE_NAME", "Nrx")
BOT_USERNAME = getenv("BOT_USERNAME", "nrx_ro_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "nrx_ro_bot")
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

