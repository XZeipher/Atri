from PyCharacterAI import Client as Sex
from pyrogram import *

token = 'b7a5cf786e6a740638c1b46ad02b035c39d96943'
auth = False

@Client.on_message(filters.me & filters.text, group=5)
async def chat(ctk,message):
    global auth,token
    client = Sex()
    if message.text.lower().startswith("atri"):
        if not auth:
            await client.authenticate_with_token(token)
            auth = True
        character_id = "Km_81EXBw_-QSRq1JcAut7jqYUfGhLNcUVO9Ms5xYwQ"
        chat = await client.create_or_continue_chat(character_id)
        message = f"Rishav: {message.text}"
        answer = await chat.send_message(message)
        return await ctk.send_message(message.chat.id,f"{answer.src_character_name}: {answer.text}")
    return
