"""Emoji

Available Commands:

.padmin"""

from telethon import events

import asyncio
from Extre import CMD_HELP
from Extre.utils import extremepro_cmd

from Extre import ALIVE_NAME
from Extre.utils import extremepro_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Extre USER"


@client.on(extremepro_cmd(pattern=f"padmin", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 20)

    await event.edit("promoting.......")

    animation_chars = [
        
            "**Promoting User As Admin...**",
            "**Enabling All Permissions To User...**",
            "**(1) Send Messages: ☑️**",
            "**(1) Send Messages: ✅**",
            "**(2) Send Media: ☑️**",
            "**(2) Send Media: ✅**",
            "**(3) Send Stickers & GIFs: ☑️**",
            "**(3) Send Stickers & GIFs: ✅**",    
            "**(4) Send Polls: ☑️**",
            "**(4) Send Polls: ✅**",
            "**(5) Embed Links: ☑️**",
            "**(5) Embed Links: ✅**",
            "**(6) Add Users: ☑️**",
            "**(6) Add Users: ✅**",
            "**(7) Pin Messages: ☑️**",
            "**(7) Pin Messages: ✅**",
            "**(8) Change Chat Info: ☑️**",
            "**(8) Change Chat Info: ✅**",
            "**Permission Granted Successfully**",
            f"**pRoMooTeD SuCcEsSfUlLy bY: {DEFAULTUSER}**"

 ]

    for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 20])
