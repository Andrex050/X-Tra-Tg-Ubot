"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "hack":

        await event.edit(input_str)

        animation_chars = [
        
            "**🔁 Connessione al server...**",
            "**💭 Utente trovato.**",
            "**🔁 Hacking...** 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "**🔁 Hacking...** 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "**🔁 Hacking...** 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",    
            "**🔁 Hacking...** 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "**🔁 Hacking...** 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "**🔁 Hacking...** 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "**🔁 Hacking...** 84%\n█████████████████████▒▒▒▒ ",
            "**🔁 Hacking...** 100%\n█████████Hacked███████████ ",
            "**👨🏼‍💻 Account Hackerato!** \n\n**⚙️ Per riavere il tuo account dovrai inviare 74€ a** @zNotASH**, oppure cercare di corrompere** `@NickAndDeath` **con dei nudes gay!**"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])
