from typing import Callable, Any, Awaitable, Dict, Union

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import ScalarResult
from sqlalchemy import select
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from db import User


class RegisterCheck(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Dict[str, Any]
    ) -> Any:
        
        if event.web_app_data:
            return await handler(event, data)

        session_nmaker = data['session_maker']
        user = event.from_user


        if not await is_user_exists(user_id=event.from_user.id, session_maker=session_maker, redis=redis):
            await create_user(user_id=event.from_user.id,
                              username=event.from_user.username, session_maker=session_maker, locale=user.language_code)
            await data['bot'].send_message(event.from_user.id, 'Ты успешно зарегистрирован(а)!')

        return await handler(event, data)
