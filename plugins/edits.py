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


@Andencento.on(admin_cmd(pattern=r"candy"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🍦🍧🍩🍪🎂🍰🧁🍫🍬🍭"))
    for _ in range(999):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)


@Andencento.on(admin_cmd(pattern=r"nothappy"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😁☹️😁☹️😁☹️😁"))
    for _ in range(999):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)


@Andencento.on(admin_cmd(pattern=r"heart"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(999):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)


@Andencento.on(admin_cmd(pattern=r"tlol"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🤔🧐🤨🤔🧐🤨"))
    for _ in range(999):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)


@Andencento.on(admin_cmd(pattern=r"lol"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😂🤣😂🤣😂🤣"))
    for _ in range(999):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)
