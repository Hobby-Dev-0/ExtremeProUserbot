# MADE BY PERRY_XD, AMAN PANDEY AND GODBOYX
# KANG WITH CREDITS 

"""
Syntax: .alive
"""


import asyncio
import os
import random
from telethon import events, TelegramClient
from Extre import *
from Extre.utils import *
from telethon.tl.types import ChannelParticipantsAdmins
from Extre import ALIVE_NAME, StartTime
from plugins import *
from Extre.utils import extremepro_cmd as extremepro_cmd, amanpandey_cmd as amanpandey_cmd
"""
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba"
EXTREMEPRO_PIC = os.environ.get("EXTREMEPRO_PIC", None) or "https://telegra.ph/file/75520b56df7b9159438cb.jpg"
EXTREMEPRO = f"**`Owner`: {DEFAULTUSER}`**\n\n"
EXTREMEPRO = f" ┏━━━━━━━━━━━━━━━━━━━\n"
EXTREMEPRO += f"┣•➳➠ `σωηєя :` `{DEFAULTUSER}` \n"
EXTREMEPRO += f"┣•➳➠ `𝓣𝓮𝓵𝓮𝓽𝓱𝓸𝓷 𝓥𝓮𝓻𝓼𝓲𝓸𝓷 :` `1.21.1` \n"
EXTREMEPRO += f"┣•➳➠ `𝐸𝓍𝓉𝓇𝑒𝓂𝑒𝒫𝓇𝑜 𝒱𝑒𝓇𝓈𝒾𝑜𝓃 :` `0.0.1`\n"
EXTREMEPRO += f"┣•➳➠ `𝓟𝔂𝓽𝓱𝓸𝓷 𝓥𝓮𝓻𝓼𝓲𝓸𝓷 :` `3.9.5`\n"
EXTREMEPRO += f"┣•➳➠ `𝔖𝔲𝔭𝔭𝔬𝔯𝔱 :` [𝔖𝔲𝔭𝔭𝔬𝔯𝔱](https://t.me/ExtremeProuserbotsupport)\n"
EXTREMEPRO += f"┣•➳➠ `υρтιмє :` `{StartTime}` \n"
EXTREMEPRO += f"┣•➳➠ `яєρσ🔥 :` [яєρσ🔥](https://github.com/TeamExtremePro/ExtremeProUserbot)\n"
EXTREMEPRO += f"┣•➳➠ `ɖɛքʟօʏ⚡ :` [ɖɛքʟօʏ⚡Me](https://dashboard.heroku.com/new?button-url=https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FTeamExtremePro%2FDeploy&template=https%3A%2F%2Fgithub.com%2FTeamExtremePro%2FDeploy)\n"
EXTREMEPRO += f"┗━━━━━━━━━━━━━━━━━━━\n"

"""
import time
from datetime import datetime as dt
from platform import python_version as pyver

from git import Repo
from Extre.version import __version__ as eVer
from Extre.version import *
from telethon import __version__, events
from telethon.errors.rpcerrorlist import ChatSendMediaForbiddenError

extreme_version = "0.1"

ExtremeVer = "0.34"
pyver = "0.34"
OWNER_NAME = os.environ.get("ALIVE_NAME", None)
OWNER_ID = os.environ.get("OWNER_ID", None)
@extremepiro_cmd(
    pattern="alive$",
)
async def lol(ult):
    pic = ExtremedB.get("ALIVE_PIC")
    uptime = time_formatter((time.time() - start_time) * 1000)
    header = ExtremedB.get("ALIVE_TEXT") if ExtremedB.get("ALIVE_TEXT") else "Hey,  I am alive."
    y = Repo().active_branch
    xx = Repo().remotes[0].config_reader.get("url")
    rep = xx.replace(".git", f"/tree/{y}")
    kk = f" `[{y}]({rep})` "
    als = (get_string("alive_1")).format(
        header,
        OWNER_NAME,
        extreme_version,
        eVer,
        uptime,
        pyver(),
        __version__,
        kk,
    )
    if pic is None:
        return await eor(ult, als)
    elif pic is not None and "telegra" in pic:
        try:
            await ult.reply(als, file=pic, link_preview=False)
            await ult.delete()
        except ChatSendMediaForbiddenError:
            await eor(ult, als, link_preview=False)
    else:
        try:
            await ult.reply(file=pic)
            await ult.reply(als, link_preview=False)
            await ult.delete()
        except ChatSendMediaForbiddenError:
            await eor(ult, als, link_preview=False)
@client.on(extremepro_cmd(outgoing=True, pattern="alive$"))
async def up(iampro):
    if iampro.fwd_from:
        return
    await iampro.get_chat()
    await iampro.delete()
    await client.send_file(op.chat_id, EXTREMEPRO_PIC, caption=EXTREMEPRO)
    await iampro.delete() 
