from pyrogram import *
from Robot.__main__ import Bot

@Bot.on_message(filters.command("me") & filters.me)
async def test(ctk,msg):
    return await ctk.send_message(msg.chat.id,"nigga")
