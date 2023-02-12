import os

import asyncio
from dotenv import load_dotenv

from bot.db import DB


load_dotenv()
token = os.getenv("BOT_TOKEN")
dsn = os.getenv("DATABASE_URL")

loop = asyncio.get_event_loop()
db = DB(
    dsn=dsn,
    loop=loop,
    pool=None
)
