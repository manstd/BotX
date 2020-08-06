import platform
import sys
import time
from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from datetime import datetime
from os import remove
from platform import python_version, uname
from shutil import which

import psutil
from telethon import __version__, version

from userbot import ALIVE_NAME, CMD_HELP, IMG, StartTime, bot
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern=r"^\.spc")
async def psu(event):
    uname = platform.uname()
    softw = "**System Information**\n"
    softw += f"`System   : {uname.system}`\n"
    softw += f"`Release  : {uname.release}`\n"
    softw += f"`Version  : {uname.version}`\n"
    softw += f"`Machine  : {uname.machine}`\n"
    # Boot Time
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"`Boot Time: {bt.day}/{bt.month}/{bt.year}  {bt.hour}:{bt.minute}:{bt.second}`\n"
    # CPU Cores
    cpuu = "**CPU Info**\n"
    cpuu += "`Physical cores   : " + \
        str(psutil.cpu_count(logical=False)) + "`\n"
    cpuu += "`Total cores      : " + \
        str(psutil.cpu_count(logical=True)) + "`\n"
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    cpuu += f"`Max Frequency    : {cpufreq.max:.2f}Mhz`\n"
    cpuu += f"`Min Frequency    : {cpufreq.min:.2f}Mhz`\n"
    cpuu += f"`Current Frequency: {cpufreq.current:.2f}Mhz`\n\n"
    # CPU usage
    cpuu += "**CPU Usage Per Core**\n"
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        cpuu += f"`Core {i}  : {percentage}%`\n"
    cpuu += "**Total CPU Usage**\n"
    cpuu += f"`All Core: {psutil.cpu_percent()}%`\n"
    # RAM Usage
    svmem = psutil.virtual_memory()
    memm = "**Memory Usage**\n"
    memm += f"`Total     : {get_size(svmem.total)}`\n"
    memm += f"`Available : {get_size(svmem.available)}`\n"
    memm += f"`Used      : {get_size(svmem.used)}`\n"
    memm += f"`Percentage: {svmem.percent}%`\n"
    # Bandwidth Usage
    bw = "**Bandwith Usage**\n"
    bw += f"`Upload  : {get_size(psutil.net_io_counters().bytes_sent)}`\n"
    bw += f"`Download: {get_size(psutil.net_io_counters().bytes_recv)}`\n"
    help_string = f"{str(softw)}\n"
    help_string += f"{str(cpuu)}\n"
    help_string += f"{str(memm)}\n"
    help_string += f"{str(bw)}\n"
    help_string += "**Engine Info**\n"
    help_string += f"`Python {sys.version}`\n"
    help_string += f"`Telethon {__version__}`"
    await event.edit(help_string)


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor



CMD_HELP.update({">`.spc`"
                 "\nUsage: Show system specification."})