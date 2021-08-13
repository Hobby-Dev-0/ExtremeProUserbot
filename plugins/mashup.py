#created by @Mr_Hops
"""video meme mashup: Avaible commands: .mash <text>
"""


import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from Extre.utils import admin_cmd


@client.on(admin_cmd(pattern="mash ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    input_str = event.pattern_match.group(1)
    reply_message = await event.get_reply_message()
    chat = "@vixtbot"
    await event.edit("```Checking...```")
    async with event.Andencento.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=285336877))
              await event.Andencento.send_message(chat, "{}".format(input_str))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Unblock @vixtbot```")
              return
          if response.text.startswith("I can't find that"):
             await event.edit("😐")
          else: 
             await event.delete()
             await event.Andencento.send_message(event.chat_id, response.message)
