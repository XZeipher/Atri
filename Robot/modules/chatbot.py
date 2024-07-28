from PyCharacterAI import Client as Sex
from pyrogram import *

client = Sex()
token = 'b7a5cf786e6a740638c1b46ad02b035c39d96943'

@Client.on_message(filters.me & filters.text)
async def chat(client,message):
    if message.text.lower.startswith("atri"):
        await client.authenticate_with_token(token)
        character_id = "Km_81EXBw_-QSRq1JcAut7jqYUfGhLNcUVO9Ms5xYwQ"
        chat = await client.create_or_continue_chat(character_id)
        message = f"Rishav: {message.text}"
        answer = await chat.send_message(message)
        return await client.send_message(message.chat.id,f"{answer.src_character_name}: {answer.text}")
    return
