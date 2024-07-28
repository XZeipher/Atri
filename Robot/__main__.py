from Robot import *
from pyrogram import *
import asyncio

loop = asyncio.get_event_loop()

async def execute():
    print("Started")
    idle()
if __name__ == "__main__":
    loop.run_until_complete(execute())
