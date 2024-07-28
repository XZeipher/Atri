from Robot import bot
from pyrogram import *

@bot.on_message(filters.me)
async def echo(client,message):
    if message.text.startswith("echo"):
        text = message.text.split("echo")[1].strip()
        return await client.send_message(chat_id=message.chat.id,text=text)
    return
