# (c) @UniBorg

from telethon import events
import asyncio
from collections import deque
from Extre.utils import admin_cmd

@client.on(admin_cmd(pattern=r"lul"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("😂🤣😂🤣😂🤣"))
	for _ in range(999):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)