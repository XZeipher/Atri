from pyrogram import *

@Client.on_message(filters.command("me", prefixes=["/","."]) and filters.me)
async def test(ctk,msg):
    return await ctk.send_message(msg.chat.id,"nigga")
