# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to the \
    Information Superhighway(yes, Internet). """

from datetime import datetime

import speedtest
from telethon import functions

from userbot import CMD_HELP
from userbot.events import register, errors_handler


@register(outgoing=True, pattern="^.speed$")
@errors_handler
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    if not spd.text[0].isalpha() and spd.text[0] not in ("/", "#", "@", "!"):
        await spd.edit("**🔄 Speed test in corso . . .**")
        test = speedtest.Speedtest()

        test.get_best_server()
        test.download()
        test.upload()
        test.results.share()
        result = test.results.dict()

    await spd.edit(""
                   " **✅ Speed test effettuato con successo!**\n"
				   "\n"
                   "**• ⬇️ Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "**• ⬆️ Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "**• 💭 Ping:** "
                   f"`{result['ping']}` \n"
                   "**• 📚 Host:** "
                   f"`{result['client']['isp']}`"
                   "")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^.nearestdc$")
@errors_handler
async def neardc(event):
    """ For .nearestdc command, get the nearest datacenter information. """
    result = await event.client(functions.help.GetNearestDcRequest())
    await event.edit(f"Città : `{result.country}` \n"
                     f"DC : `{result.nearest_dc}` \n"
                     f"DC : `{result.this_dc}`")
