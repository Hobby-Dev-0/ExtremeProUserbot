# (c) @TeleBotHelp and @ExtremeProUserbot_Official
# By @xditya. Kangers keep credits xD
# All in one code.

"""TeleBot
Available Commands:
.tlol
.lol
.heart
.candy
.nothappy"""

import asyncio
from collections import deque

from Extre.utils import admin_cmd


@client.on(admin_cmd(pattern=r"candy"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("๐ฆ๐ง๐ฉ๐ช๐๐ฐ๐ง๐ซ๐ฌ๐ญ"))
    for _ in range(999):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)


@client.on(admin_cmd(pattern=r"nothappy"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("๐โน๏ธ๐โน๏ธ๐โน๏ธ๐"))
    for _ in range(999):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)


@client.on(admin_cmd(pattern=r"heart"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("โค๏ธ๐งก๐๐๐๐๐ค"))
    for _ in range(999):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)


@client.on(admin_cmd(pattern=r"tlol"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("๐ค๐ง๐คจ๐ค๐ง๐คจ"))
    for _ in range(999):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)


@client.on(admin_cmd(pattern=r"lol"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("๐๐คฃ๐๐คฃ๐๐คฃ"))
    for _ in range(999):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)
