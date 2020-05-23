"""Emoji

Available Commands:

.padmin"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 20)

    input_str = event.pattern_match.group(1)

    if input_str == "padmin":

        await event.edit(input_str)

        animation_chars = [
        
            "**🔁 Sto promuovendo l'Utente ad Admin...**",
            "**🔁 Abilitando tutti i permessi...**",
            "**(1) Inviare messaggi: ☑️**",
            "**(1) Inviare messaggi: ✅**",
            "**(2) Inviare Media: ☑️**",
            "**(2) Inviare Media: ✅**",
            "**(3) Inviare Stickers & GIFs: ☑️**",
            "**(3) Inviare Stickers & GIFs: ✅**",    
            "**(4) Inviare Polls: ☑️**",
            "**(4) Inviare Polls: ✅**",
            "**(5) Aggiungere Link: ☑️**",
            "**(5) Aggiungere Link: ✅**",
            "**(6) Aggiungere Membri: ☑️**",
            "**(6) Aggiungere Membri: ✅**",
            "**(7) Fissare Messaggi: ☑️**",
            "**(7) Fissare Messaggi: ✅**",
            "**(8) Cambiare info della chat: ☑️**",
            "**(8) Cambiare info della chat: ✅**",
            "**💭 Utente promosso ad Admin!**",
            "**Bro.. stavo scherzando.. Sorry.. 😭**"

 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 20])
