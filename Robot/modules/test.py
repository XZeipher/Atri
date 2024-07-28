from pyrogram import *

@Client.on_message(filters.command("me"))
async def test(_,msg):
    return await msg.reply_text("nigga")
