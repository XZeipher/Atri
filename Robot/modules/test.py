from pyrogram import *
from Robot.__main__ import Bot

@Bot.on_message(filters.command("me") & filters.me)
async def test(_,msg):
    return await msg.reply_text("nigga")
