import os
import logging

import asyncio
from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy.engine import URL

from commands import register_user_commands, bot_commands
from db.db import initial_creation
# from db import BaseModel, create_async_engine, get_session_maker, proceed_schemas
# from db.db_commands import DataBase

logging.basicConfig(
    filename='log.log', 
    level=logging.INFO,
    format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
)


async def main() -> None:
    commands_for_bot = []
    await initial_creation()

    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))

    dp = Dispatcher()
    bot = Bot(token=os.getenv('BOT_TOKEN'), parse_mode='HTML')
    await bot.set_my_commands(commands=commands_for_bot)

    register_user_commands(dp)
    # postgres_url = URL.create(
    #     'postgresql+asyncpg',
    #     host='localhost',
    #     username=os.getenv('db_user'),
    #     database=os.getenv('db_name'),
    #     password=os.getenv('db_pass'),
    #     port=os.getenv('db_port')
    # )

    # async_engine = create_async_engine(postgres_url)
    # session_maker = get_session_maker(async_engine)
    # await proceed_schemas(async_engine, BaseModel.metadata)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped!!!')
