from Robot import *
from pyrogram import *
import asyncio
import logging

FORMAT = "[SERVER] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)

LOGGER = logging.getLogger('[Atri - By Alpha Coder]')

class Bot(Client):
    def __init__(self):
        LOGGER.info("Executing...")
        super().__init__(
            "atri",
            api_id=api_id,
            api_hash=api_hash,
            session_string=session_string,
            plugins={"root": "Robot.modules"},
        )
    async def start(self):
        await super().start()
        LOGGER.info("Started")
        await super().send_message("StackHostSupport","Started")

    async def stop(self):
        await super().stop()

if __name__ == "__main__":
    Bot().run()
