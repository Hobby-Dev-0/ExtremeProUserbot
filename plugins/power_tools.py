"""Restart or Terminate the bot from any chat
Available Commands:
.restartsys
.shutdown"""
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html
from telethon import events
import asyncio
import os
import sys
from Extre.utils import admin_cmd

from var import Var

from plugins import *


@client.on(admin_cmd(pattern="restart"))
async def restartbt(ult):
    ok = await eor(ult, "āš¢š°š±ššÆš±š¢š” šš¬š²šÆ šš¬š±ā \nšš¬`.šš©š¦š³š¢`  š¬šÆ `.š„š¢š©š­šŖš¢` šš£š±š¢šÆ 5 šŖš¦š«š²š±š¢š° š¬š£ šÆš¢š°š±ššÆš±š¦š«š¤ š­šÆš¬š š¢š°š° š±š¬ š š„š¢š šØ š¦š£ ā ššŖ š¬š«š©š¦š«š¢")
    if Var.HEROKU_API_KEY:
        await bash("pkill python3 && python3 -m Extre")


@client.on(admin_cmd(pattern="shutdown"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Turning off ...Manually turn me on later")
    await borg.disconnect()
