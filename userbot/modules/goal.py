from telethon.tl.types import InputMediaDice
from userbot.events import register 
from userbot import CMD_HELP



@register(outgoing=True, pattern="^.goll(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice('⚽'))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice(''))
        except:
            pass
            
            
CMD_HELP.update({
    "gol":
    "`.goll` 1-6\
\nUsage: hahaha just a magic.\nWarning:`Don't use any other values or bot will crash`"
})    
