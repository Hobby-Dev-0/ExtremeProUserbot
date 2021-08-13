# MAKING IT EASIEST FOR EXTREME PRO USERBOT
# THIS FILE IS PART OF https://github.com/TeamExtremePro/ExtremeProUserbot.git
import asyncio
import os
from telethon import TelegramClient
extremepro_version = "0.1"
from telethon.sessions import StringSession
from Extre.connections import client_connection, redis_connection
from Extre import *
from Extre import *
from Extre.core import *
CMD_HELP_BOT = {}
from Extre.utils import *
from Extre._wrappers import *
from Extre.func import *
from strings import get_string
from Extre.core import *
from Extre.sudo import *
from Extre.extremecmd import *
from Extre.config import Config
from Extre.var import Var
from Extre.variables import Var
from Extre import CMD_LIST, CMD_HELP, CMD_HELP_BOT, BRAIN_CHECKER, INT_PLUG, LOAD_PLUG, COUNT_MSG, USERS, COUNT_PM, LASTMSG, CMD_HELP, ISAFK, AFKREASON, SUDO_LIST
AUTONAME = os.environ.get("AUTONAME", None)
from telethon.tl.types import Channel


import asyncio
import time

from Extre import *
from Extre.dB import *
from Extre.functions.all import *
from Extre.functions.sudos import *
from Extre.version import *
from telethon import Button
from telethon.tl import functions, types


start_time = time.time()

OWNER_NAME = extremepro_bot.me.first_name
OWNER_ID = extremepro_bot.me.id

List = []
Dict = {}
N = 0

NOSPAM_CHAT = [
    -1001387666944,  # @PyrogramChat
    -1001109500936,  # @TelethonChat
    -1001050982793,  # @Python
    -1001256902287,  # @DurovsChat
]


from Extre import *
from Extre import *
from Extre import ALIVE_NAME, bot
PMSECURITY = os.environ.get("PMSECURITY", None)
bot = Andencento
uptime = "dekhna jaruri hai kya"

Eiva_USER = "Andencento User"
ForGo10God = "-100"
Eiva_mention = f"[{Eiva_USER}](tg://user?id={ForGo10God})"

Andencento_USER = "Andencento"
Andencento_mention = f"[{Andencento_USER}](tg://user?id={ForGo10God})"
hl = os.environ.get("HANDLER", None) or "."
shl = os.environ.get("SUDO_HANDLER", None) or "."
Andencento_ver = "0.1"
tel_ver = "0.1"
devs = ""
user_mention = Andencento_mention

import os

from Extre import CMD_HELP

chnl_link = "https://t.me/Andencento"

COMMAND_HAND_LER = os.environ.get("HANDLER", ".")

#################################################################################################################


class CmdHelp:
    """
    The class I wrote to better generate command aids.
    """

    FILE = ""
    ORIGINAL_FILE = ""
    FILE_AUTHOR = ""
    IS_OFFICIAL = True
    COMMANDS = {}
    PREFIX = COMMAND_HAND_LER
    WARNING = ""
    INFO = ""

    def __init__(self, file: str, official: bool = True, file_name: str = None):
        self.FILE = file
        self.ORIGINAL_FILE = file
        self.IS_OFFICIAL = official
        self.FILE_NAME = file_name if not file_name == None else file + ".py"
        self.COMMANDS = {}
        self.FILE_AUTHOR = ""
        self.WARNING = ""
        self.INFO = ""

    def set_file_info(self, name: str, value: str):
        if name == "name":
            self.FILE = value
        elif name == "author":
            self.FILE_AUTHOR = value
        return self

    def add_command(self, command: str, params=None, usage: str = "", example=None):
        """
        Inserts commands..
        """

        self.COMMANDS[command] = {
            "command": command,
            "params": params,
            "usage": usage,
            "example": example,
        }
        return self

    def add_warning(self, warning):
        self.WARNING = warning
        return self

    def add_info(self, info):
        self.INFO = info
        return self

    def get_result(self):
        """
        Brings results.
        """

        result = f"**📗 File :** `{self.FILE}`\n"
        if self.WARNING == "" and self.INFO == "":
            result += f"**⬇️ Official:** {'✅' if self.IS_OFFICIAL else '❌'}\n\n"
        else:
            result += f"**⬇️ Official:** {'✅' if self.IS_OFFICIAL else '❌'}\n"

            if self.INFO == "":
                if not self.WARNING == "":
                    result += f"**⚠️ Warning :** {self.WARNING}\n\n"
            else:
                if not self.WARNING == "":
                    result += f"**⚠️ Warning :** {self.WARNING}\n"
                result += f"**ℹ️ Info:** {self.INFO}\n\n"

        for command in self.COMMANDS:
            command = self.COMMANDS[command]
            if command["params"] == None:
                result += (
                    f"**🛠 Command :** `{COMMAND_HAND_LER[:1]}{command['command']}`\n"
                )
            else:
                result += f"**🛠 Command :** `{COMMAND_HAND_LER[:1]}{command['command']} {command['params']}`\n"

            if command["example"] == None:
                result += f"**💬 Details :** `{command['usage']}`\n\n"
            else:
                result += f"**💬 Details :** `{command['usage']}`\n"
                result += f"**⌨️ For Example :** `{COMMAND_HAND_LER[:1]}{command['example']}`\n\n"
        return result

    def add(self):
        """
        Directly adds CMD_HELP.
        """
        CMD_HELP_BOT[self.FILE] = {
            "info": {
                "official": self.IS_OFFICIAL,
                "warning": self.WARNING,
                "info": self.INFO,
            },
            "commands": self.COMMANDS,
        }
        CMD_HELP[self.FILE] = self.get_result()
        return True

    def getText(self, text: str):
        if text == "REPLY_OR_USERNAME":
            return "<user name> <user name/answer >"
        elif text == "OR":
            return "or"
        elif text == "USERNAMES":
            return "<user name (s)>"

async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid

extremeprover = "0.1"
# stats
if Var.PRIVATE_GROUP_ID:
    log = "Enabled"
else:
    log = "Disabled"

if Config.TG_BOT_USER_NAME_BF_HER:
    bots = "Enabled"
else:
    bots = "Disabled"

if Var.LYDIA_API_KEY:
    lyd = "Enabled"
else:
    lyd = "Disabled"

if Config.SUDO_USERS:
    sudo = "Disabled"
else:
    sudo = "Enabled"

if Config.PMSECURITY.lower() == "off":
    pm = "Disabled"
else:
    pm = "Enabled"

TELEUSER = str(ALIVE_NAME) if ALIVE_NAME else "EXTREMEPRO USER"

extremepro = f"EXTREMEPRO Version: {extremeprover}\n"
extremepro += f"Log Group: {log}\n"
extremepro += f"Assistant Bot: {bots}\n"
extremepro += f"Lydia: {lyd}\n"
extremepro += f"Sudo: {sudo}\n"
extremepro += f"PMSecurity: {pm}\n"
extremepro += f"\nVisit @EXTREMEPRO USERBOT for assistance.\n"
extremeprostats = f"{extremepro}"

EXTREMEPRO_NAME = ALIVE_NAME
OWNER_ID = os.environ.get("OWNER_ID", None)

# count total number of groups
from Extre import *

async def extremepro_grps(event):
    a = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel):
            if entity.megagroup:
                if entity.creator or entity.admin_rights:
                    a.append(entity.id)
    return len(a), a




async def bash(cmd):
    process = await asyncio.create_subprocess_suser(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    err = stderr.decode().strip()
    out = stdout.decode().strip()
    return out, err


def time_formatter(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + " day(s), ") if days else "")
        + ((str(hours) + " hour(s), ") if hours else "")
        + ((str(minutes) + " minute(s), ") if minutes else "")
        + ((str(seconds) + " second(s), ") if seconds else "")
        + ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    )
    return tmp[:-2]
