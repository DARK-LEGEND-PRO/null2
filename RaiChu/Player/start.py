import asyncio
from time import time
from datetime import datetime
from RaiChu.config import BOT_USERNAME, OWNER_USERNAME, START_PIC
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_PIC}",
        caption=f"""**ʜɪɪ, ɪ ᴍ ᴀ ꜱɪᴍᴘʟᴇ ᴍᴜꜱɪᴄ ʙᴏᴛ ɪ ᴄᴀɴ ᴘʟᴀʏ   ᴍᴜꜱɪᴄ ᴀɴᴅ ᴠɪᴅᴇᴏꜱ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ...
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ᴏᴡɴᴇʀ ✨", url=f"https://t.me/{OWNER_USERNAME}"
                    ),
                ],
                
           ]
        ),
    )
    
    

