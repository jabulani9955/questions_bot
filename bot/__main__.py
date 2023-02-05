import logging

import asyncio
from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand

from bot.commands import register_user_commands, bot_commands
from bot.db.loader import token, db


logging.basicConfig(
    filename='log.log', 
    level=logging.INFO,
    format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
)


async def main() -> None:
    await db.initial_creation()
    
    dp = Dispatcher()
    bot = Bot(token=token, parse_mode='HTML')
    
    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))
    
    await bot.set_my_commands(commands=commands_for_bot)

    register_user_commands(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        pass
