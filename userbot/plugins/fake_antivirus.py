from telethon import events
import asyncio

@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 11)
    input_str = event.pattern_match.group(1)
    if input_str == "novirus":
        await event.edit(input_str)
        animation_chars = [
        
            "**🔁 Sto scaricando il file..**",
            "**📚 File scaricato.**",
            "**🔁 Scansione totale in corso..**\n\n\n**ℹ️ Iscrizione:** `Utente Pro`\n**📆 Valido fino a:** `31/12/2099`\n\n**🔁 Scan in corso...** `0%`\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "**🔁 Scansione totale in corso..**\n\n\n**ℹ️ Iscrizione:** `Utente Pro`\n**📆 Valido fino a:** `31/12/2099`\n\n**🔁 Scan in corso...** `4%`\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "**🔁 Scansione totale in corso..**\n\n\n**ℹ️ Iscrizione:** `Utente Pro`\n**📆 Valido fino a:** `31/12/2099`\n\n**🔁 Scan in corso...** `8%`\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",    
            "**🔁 Scansione totale in corso..**\n\n\n**ℹ️ Iscrizione:** `Utente Pro`\n**📆 Valido fino a:** `31/12/2099`\n\n**🔁 Scan in corso...** `20%`\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "**🔁 Scansione totale in corso..**\n\n\n**ℹ️ Iscrizione:** `Utente Pro`\n**📆 Valido fino a:** `31/12/2099`\n\n**🔁 Scan in corso...** `36%`\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "**🔁 Scansione totale in corso..**\n\n\n**ℹ️ Iscrizione:** `Utente Pro`\n**📆 Valido fino a:** `31/12/2099`\n\n**🔁 Scan in corso...** `52%`\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "**🔁 Scansione totale in corso..**\n\n\n**ℹ️ Iscrizione:** `Utente Pro`\n**📆 Valido fino a:** `31/12/2099`\n\n**🔁 Scan in corso...** `84%`\n█████████████████████▒▒▒▒ ",
            "**🔁 Scansione totale in corso..**\n\n\n**ℹ️ Iscrizione:** `Utente Pro`\n**📆 Valido fino a:** `31/12/2099`\n\n**🔁 Scan in corso...** `100%`\n█████████████████████████ ",
            "**🔁 Scansione totale in corso..**\n\n\n**ℹ️ Iscrizione:** `Utente Pro`\n**📆 Valido fino a:** `31/12/2099`\n\n**📚 File completati:** `01`/`01`\n\n**⚠️ Risultati:** `Nessun virus trovato!`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "virus":

        await event.edit(input_str)

        animation_chars = [
        
            "**🔁 Sto scaricando il file..**",
            "**📚 File scaricato.**",
            "**🔁 Scansione totale in corso..**\n\n\n**ℹ️ Iscrizione:** `Utente Pro`\n**📆 Valido fino a:** `31/12/2099`\n\n**🔁 Scan in corso...** `0%`\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "**🔁 Scansione totale in corso..**\n\n\n**ℹ️ Iscrizione:** `Utente Pro`\n**📆 Valido fino a:** `31/12/2099`\n\n**🔁 Scan in corso...** `4%`\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "**🔁 Scansione totale in corso..**\n\n\n**ℹ️ Iscrizione:** `Utente Pro`\n**📆 Valido fino a:** `31/12/2099`\n\n**🔁 Scan in corso...** `8%`\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",    
            "**🔁 Scansione totale in corso..**\n\n\n**ℹ️ Iscrizione:** `Utente Pro`\n**📆 Valido fino a:** `31/12/2099`\n\n**🔁 Scan in corso...** `20%`\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "**🔁 Scansione totale in corso..**\n\n\n**ℹ️ Iscrizione:** `Utente Pro`\n**📆 Valido fino a:** `31/12/2099`\n\n**🔁 Scan in corso...** `36%`\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "**🔁 Scansione totale in corso..**\n\n\n**ℹ️ Iscrizione:** `Utente Pro`\n**📆 Valido fino a:** `31/12/2099`\n\n**🔁 Scan in corso...** `52%`\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "**🔁 Scansione totale in corso..**\n\n\n**ℹ️ Iscrizione:** `Utente Pro`\n**📆 Valido fino a:** `31/12/2099`\n\n**🔁 Scan in corso...** `84%`\n█████████████████████▒▒▒▒ ",
            "**🔁 Scansione totale in corso..**\n\n\n**ℹ️ Iscrizione:** `Utente Pro`\n**📆 Valido fino a:** `31/12/2099`\n\n**🔁 Scan in corso...** `100%`\n█████████████████████████ ",
            "**🔁 Scansione totale in corso..**\n\n\n**ℹ️ Iscrizione:** `Utente Pro`\n**📆 Valido fino a:** `31/12/2099`\n\n**📚 File completati:** `01`/`01`\n\n**⚠️ Risultati:** `Virus trovati! (Worm, Trojan, Spyware, Adware, Exploit, Rootkit, Rogues / Scareware)`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])
