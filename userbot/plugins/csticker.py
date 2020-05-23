import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="csticker ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("❌** Errore:** `Rispondi ad un messaggio!`")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("❌** Errore:** `Rispondi ad un messaggio di testo!`")
       return
    chat = "@QuotLyBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("❌** Errore:** `Rispondi ad un messaggio!`")
       return
    await event.edit("**🔁 Creando lo sticker...**")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1031952739))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("❌** Errore:** `Sblocca` @QuotLyBot.")
              return
          if response.text.startswith("Hi!"):
             await event.edit("❌** Errore:** `Disabilita le impostazioni di inoltro. ")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)