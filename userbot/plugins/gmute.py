from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
import asyncio

@command(outgoing=True, pattern=r"^.gmute ?(\d+)?")
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("**🔁 Caricamento ...**")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("**🔁 Caricamento ...**")
    chat_id = event.chat_id
    chat = await event.get_chat()
    if is_muted(userid, "gmute"):
        return await event.edit("**💭 Questo utente è già mutato!**")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await event.edit("**❌ ERRORE!**\nℹ️ **Errore:** " + str(e))
    else:
        await event.edit("**🔇 Utente mutato globalmente!**")

@command(outgoing=True, pattern=r"^.ungmute ?(\d+)?")
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("**🔁 Caricamento ...**")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("**❌ Perfavore rispondi ad un messaggio.**")
    chat_id = event.chat_id
    if not is_muted(userid, "gmute"):
        return await event.edit("**💭 Questo utente è già mutato!*")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await event.edit("**❌ ERRORE!**\nℹ️ **Errore:** " + str(e))
    else:
        await event.edit("**🔊 Utente smutato correttamente!**")
@command(outgoing=True, pattern=r"^.gmute ?(\d+)?", allow_sudo=True)
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("**🔁 Caricamento ...**")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("**❌ Perfavore rispondi ad un messaggio.**")
    chat_id = event.chat_id
    chat = await event.get_chat()
    if is_muted(userid, "gmute"):
        return await event.edit("** 💭 Questo utente è già mutato!**")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await event.edit("**❌ ERRORE!**\nℹ️ **Errore:* " + str(e))
    else:
        await event.edit("**🔊 Utente smutato correttamente!**")

@command(outgoing=True, pattern=r"^.ungmute ?(\d+)?", allow_sudo=True)
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("**🔁 Caricamento ...**")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("**❌ Perfavore rispondi ad un messaggio.**")
    chat_id = event.chat_id
    if not is_muted(userid, "gmute"):
        return await event.edit("**🔊 Utente smutato correttamente!**")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await event.edit("**❌ ERRORE!**\nℹ️ **Errore:** " + str(e))
    else:
        await event.edit("** 💭 Questo utente non è mutato!**")

@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()
