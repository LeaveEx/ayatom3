from telethon import Button
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from OrekiRobot import tbot as tbot
from OrekiRobot.events import register

IMAGE = "https://te.legra.ph/file/191a2b533e49ddd8f63cc.jpg"

@register(pattern=("Varisu"))
async def awake(event):
      IMG_CAPTION = """
*Results for Varisu*
"""

BUTTON = [
     [
       InlineKeyboardButton(
       text=f"Download [285.9MB] File", callback data="file1"),
       text=f"Download [436.4MB] File", callback data="file2"),
       text=f"Download [711.1MB] File", callback data="file3"),
       text=f"Download [1.07GB] File", callback data="file4"),
       text=f"Download [1.74GB] File", callback data="file5"),
     ]
]
await tbot.send_file(event.chat_id, IMAGE, caption=IMG_CAPTION, buttons=BUTTON)

file1 = "https://t.me/OrekiMovies/6"

FILE1_CAP_OREKI = """
**Varisu (2023) HQ PreDVD - x264 - Tamil**
**➠ Uploaded by :** @OrekiProXBot
"""
@register(pattern=("Varisu"))
async def awake(event):
    await tbot.send_file(event.chat_id, file1, caption=FILE1_CAP_OREKI)


file2 = "https://t.me/OrekiMovies/7"

FILE2_CAP_OREKI = """
**Varisu (2023) HQ PreDVD - x264 - Tamil**
**➠ Uploaded by :** @OrekiProXBot
"""
@register(pattern=("Varisu"))
async def awake(event):
    await tbot.send_file(event.chat_id, file2, caption=FILE2_CAP_OREKI)


file3 = "https://t.me/OrekiMovies/8"

FILE3_CAP_OREKI = """
**Varisu (2023) HQ PreDVD - x264 - Tamil**
**➠ Uploaded by :** @OrekiProXBot
"""
@register(pattern=("Varisu"))
async def awake(event):
    await tbot.send_file(event.chat_id, file3, caption=FILE3_CAP_OREKI)


file4 = "https://t.me/OrekiMovies/9"

FILE4_CAP_OREKI = """
**Varisu (2023) HQ PreDVD - x264 - Tamil**
**➠ Uploaded by :** @OrekiProXBot
"""
@register(pattern=("Varisu"))
async def awake(event):
    await tbot.send_file(event.chat_id, file4, caption=FILE4_CAP_OREKI)


file5 = "https://t.me/OrekiMovies/10"

FILE5_CAP_OREKI = """
**Varisu (2023) HQ PreDVD - x264 - Tamil**
**➠ Uploaded by :** @OrekiProXBot
"""
@register(pattern=("Varisu"))
async def awake(event):
    await tbot.send_file(event.chat_id, file5, caption=FILE5_CAP_OREKI)



@register(pattern=("Varisu"))
async def awake(event):
  await event.reply("➠ Uploaded by : @OrekiProXBot")
