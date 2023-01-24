import datetime

from sqlalchemy import Column, Integer, VARCHAR, select, BigInteger, Enum
from sqlalchemy.orm import sessionmaker, relationship, selectinload
from sqlalchemy.exc import ProgrammingError

from .base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    # Telegram user id.
    user_id = Column(Integer, unique=True, nullable=False, primary_key=True)

    # Telegran user name.
    username = Column(VARCHAR(32), unique=False, nullable=True)

    def __str__(self) -> str:
        return f"<User: {self.user_id}>"


async def get_user(user_id: int, session_maker: sessionmaker) -> User:
    """
    Получить пользователя по его id
    :param user_id:
    :param session_maker:
    :return:
    """
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(
                select(User)
                    .options(selectinload(User.posts))
                    .filter(User.user_id == user_id)  # type: ignore
            )
            return result.scalars().one()


async def create_user(user_id: int, username: str, locale: str, session_maker: sessionmaker) -> None:
    async with session_maker() as session:
        async with session.begin():
            user = User(
                user_id=user_id,
                username=username
            )
            try:
                session.add(user)
            except ProgrammingError as e:
                # TODO: add log
                pass


async def user_exists(user_id: int, session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            sql_res = await session.execute(select(User).where(User.user_id == user_id))

            if not sql_res:
                return bool(sql_res)

# async def is_user_exists(user_id: int, session_maker: sessionmaker, redis: Redis) -> bool:
#     res = await redis.get(name='is_user_exists:' + str(user_id))
#     if not res:
#         async with session_maker() as session:
#             async with session.begin():
#                 sql_res = await session.execute(select(User).where(User.user_id == user_id))
#                 await redis.set(name='is_user_exists:' + str(user_id), value=1 if sql_res else 0)
#                 return bool(sql_res)
#     else:
#         return bool(res)
