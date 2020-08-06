""" Userbot module for having some fun with people. """
import time
from asyncio import sleep
from collections import deque
from random import choice, getrandbits, randint
from re import sub

import requests
from cowpy import cow

from userbot import CMD_HELP, LOGS
from userbot.events import register
from userbot.modules.admin import get_user_from_event

# ================= CONSTANT =================
@register(outgoing=True, pattern=r"^\.alok$")
async def repo_is_here(wannasee):
    """ For .alok command, just returns the xnxx """
    await wannasee.edit("GiVe AL0K B4ng& [iD kU](https://xnxx.com)")

@register(outgoing=True, pattern=r"^\.ibb$")
async def lol(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "IRI? BILANG BAWAHAN!🖕"
        )

@register(outgoing=True, pattern=r"^\.bct$")
async def lol(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "BACOT BAT LU BANG JAGO!🖕"
        )

@register(outgoing=True, pattern=r"^\.jago$")
async def lol(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "AMPUN BANG JAGO🙏"
        )
CMD_HELP.update(
    {
        "alok": ">`.alok`\
\nUsage: cow which says things.\
\n\n>`.alok`\
\nUsage: Copypasta the famous meme\
\n\n>`.ibb`\
\nUsage: Vaporize everything!\
\n\n>`.bct`\
\nUsage: Stretch it.\
\n\n>`.jago`\
\n\n\nThanks to 🅱️ottom🅱️ext🅱️ot (`@NotAMemeBot`) for some of these."
    }
)
