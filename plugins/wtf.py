"""Emoji
Available Commands:
.wtf"""
import asyncio

from Extre.utils import admin_cmd


@client.on(admin_cmd("wtf"))
async def _(event):
    if event.fwd_from:
        return
    animation_ttl = range(0, 5)
    await event.edit("wtf")
    animation_chars = [
        "What",
        "What The",
        "What The F",
        "What The F Brah",
        "[What The F Brah](https://telegra.ph//file/f3b760e4a99340d331f9b.jpg)",
    ]
    for i in animation_ttl:
        await asyncio.sleep(0.3)
        await event.edit(animation_chars[i])
        i += 1
