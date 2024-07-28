from Robot import *
from pyrogram import *
import asyncio


async def execute():
    print("Started")
    await idle()
if __name__ == "__main__":
    loop.run_until_complete(execute())
