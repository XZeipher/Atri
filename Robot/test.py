from pyrogram import *

@Client.on_message(filters.me & filters.command("me"))
async def test(_,msg):
    return await msg.reply_text("nigga")
