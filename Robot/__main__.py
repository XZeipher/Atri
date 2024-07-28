from Robot import *
from pyrogram import *
import asyncio

class Bot(Client):
    def __init__(self):
        super().__init__(
            "atri",
            api_id=api_id,
            api_hash=api_hash,
            session_string=session_string,
            plugins={"root": "Robot.modules"},
        )
    async def start(self):
        await super().start()
        print("started")

    async def stop(self):
        await super().stop()

if __name__ == "__main__":
    Bot().run()
