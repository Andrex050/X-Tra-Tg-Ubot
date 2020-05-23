# Lots of lub to @r4v4n4 for gibing the base <3
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd,register

@borg.on(admin_cmd("scan ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("**❌ Errore**: `Rispondi ad un messaggio.`")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit("**❌ Errore**: `Rispondi ad un media.`")
       return
    chat = "@DrWebBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("**❌ Errore**: `Rispondi al messaggio di un utente.`")
       return
    await event.edit("**🔁 Caricamento ...**")
    async with borg.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=161163358))
              await borg.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("**❌ Errore**: `Sblocca` @sangmatainfo_bot `e riprova.`")
              return
          if response.text.startswith("Forward"):
             await event.edit("**❌ Errore**: `Disabilita le impostazioni di privacy all'inoltro messaggi e riprova.")
          else:
          	if response.text.startswith("Select"):
          		await event.edit("**⚠️ Vai su** @DrWebBot **e seleziona la lingua adatta.") 
          	else: 
          			await event.edit(f"**✅ Scan completata!\n\n📚 Risultati:**\n↪️ `{response.message.message}`.")
