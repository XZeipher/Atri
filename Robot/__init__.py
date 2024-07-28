from pyrogram import *
import asyncio
loop = asyncio.get_event_loop()
bot = Client(
    "snndndndn",
    api_id=19246875,
    api_hash="54fe37d97464cfc4754ed019e53bbd9c",
    session_string="BQElrxsAM6WhtZvnCOa_8Gpez-2m6mRJ2HgqvXfln6G-82DIhO1rOtuv_38RZoD1oUtkk6876MA7joblYhUtmdQpfcIEBC4D6R02_xvYoWB60R9sPfwyMFSLoddNycnbYYaJThe40ps7aCd2Ok8I83k1k8EBpkRNaheu315shlwX90Z4aqIAKRcDOCO7f3bOSq-gKmCwYdZ0co5BXwvWQbnLSMAfcGx9ua3AdmvHFOuo0mJQv1qKZiv8ye80_7prD2GYcNjDOiyI-1LRS7PcjkLgl1fDP6NQsJO22tSO-0O8aLUwbqkWkcy9EVgp7vEuFUHbjZ2pkcdQBQ2UFftDo1y7uJ5_IwAAAAG4qLIFAA"
)

async def init():
    await bot.start()


loop.run_until_complete(init())
