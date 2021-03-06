import asyncio

import telethon.utils
from telethon import events

from Extre.utils import admin_cmd


async def get_target_message(event):
    if event.is_reply and (await event.get_reply_message()).from_id == borg.uid:
        return await event.get_reply_message()
    async for message in borg.iter_messages(await event.get_input_chat(), limit=20):
        if message.out:
            return message


async def await_read(chat, message):
    chat = telethon.utils.get_peer_id(chat)

    async def read_filter(read_event):
        return read_event.chat_id == chat and read_event.is_read(message)

    fut = borg.await_event(events.MessageRead(inbox=False), read_filter)
    if await is_read(borg, chat, message):
        fut.cancel()
        return
    await fut


@client.on(admin_cmd(pattern="(del)(?:ete)?$"))
@client.on(admin_cmd(pattern="(edit)(?:\s+(.*))?$"))
async def delete(event):
    await event.delete()
    command = event.pattern_match.group(1)
    if command == "edit":
        text = event.pattern_match.group(2)
        if not text:
            return
    target = await get_target_message(event)
    if target:
        chat = await event.get_input_chat()
        await await_read(chat, target)
        await asyncio.sleep(0.5)
        if command == "edit":
            await borg.edit_message(chat, target, text)
        else:
            await borg.delete_messages(chat, target, revoke=True)
