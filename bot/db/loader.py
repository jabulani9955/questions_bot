import os

import asyncio
from dotenv import load_dotenv

from bot.db import DB


load_dotenv()
token = os.getenv("BOT_TOKEN")

loop = asyncio.get_event_loop()
db = DB(
    name=os.getenv("POSTGRES_DB"),
    host=os.getenv("POSTGRES_HOST"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    port=os.getenv("POSTGRES_PORT"),
    loop=loop,
    pool=None
)
