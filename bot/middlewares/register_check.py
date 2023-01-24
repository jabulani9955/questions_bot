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
        
        session_maker: sessionmaker = data['session_maker']

        async with session_maker() as session:
            async with session.begin():
                session: AsyncSession
                result = await session.execute(select(User).where(User.user_id == event.from_user.id))
                result: ScalarResult
                user: User = result.one_or_none()

                if user:
                    pass
                else:
                    user = User(
                        user_id=event.from_user.id,
                        username=event.from_user.username
                    )
                    await session.merge(user)
                    if isinstance(event, Message):
                        await event.answer('Регистрация успешна.')
                    else:
                        await event.message.answer('Регистрация успешна.')
        return await handler(event, data)
