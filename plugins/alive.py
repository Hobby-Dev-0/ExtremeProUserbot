import asyncio
import random
from telethon import events, TelegramClient
from amanpandey import extremepro_cmd
from telethon.tl.types import ChannelParticipantsAdmins
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔

edit_time = 5
""" =======================CONSTANTS====================== """
PM_IMG = "https://telegra.ph/file/75520b56df7b9159438cb.jpg"
pm_caption = " ●● ExtremePro is Alive ●●\n\n"
pm_caption += "●● VERSION  :0.1 ●●\n\n"
pm_caption += "●● PYTHON : 3.9.2 ●●\n\n"
pm_caption += "●● TELETHON : 1.21.1 ●●\n\n"
pm_caption += "●● Copyright Team ExtremePro ●● :2021-2022 \n\n"
pm_caption += "●● Extreme Branch ●● :Main \n\n"

@borg.on(extremepro_cmd(pattern=r"alive"))
async def amanpandey(event):
    await borg.send_file(event.chat_id, PM_IMG, caption=pm_caption)
