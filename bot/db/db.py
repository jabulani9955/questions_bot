from asyncio import AbstractEventLoop
import asyncpg

from bot.db.queries import CREATE_QUERIES, INSERT_QUERIES, GET_QUERIES


class DB:
    def __init__(
        self,
        name: str,
        user: str,
        password: str,
        port: str,
        loop: AbstractEventLoop,
        pool: asyncpg.pool.Pool
    ) -> None:
        self.name = name
        self.user = user
        self.password = password
        self.port = port
        self.loop = loop
        self.pool = loop.run_until_complete(
            asyncpg.create_pool(
                database=name,
                user=user,
                password=password,
                port=port
            )
        )

    async def get_correct_answer(self, question_id: int) -> asyncpg.Record:
        return await self.pool.fetchrow(GET_QUERIES['GET_CORRECT_ANSWER'], question_id)

    async def get_questions_num(self) -> int:
        return await self.pool.fetchval(GET_QUERIES['GET_NUM_QUESTIONS'])

    async def get_question_by_id(self, question_id: int) -> list[asyncpg.Record]:
        return await self.pool.fetch(GET_QUERIES['GET_QUESTION_BY_ID'], question_id)

    async def is_user_exist(self, user_id: int):
        return await self.pool.fetchrow(GET_QUERIES['GET_USER_BY_ID'], user_id)

    async def initial_creation(self):
        """ Функция для первоначального создания таблиц. """

        await self.pool.execute(CREATE_QUERIES['CREATE_USERS'])
        await self.pool.execute(CREATE_QUERIES['CREATE_QUESTIONS'])
        await self.pool.execute(CREATE_QUERIES['CREATE_ANSWERS'])
        await self.pool.execute(CREATE_QUERIES['CREATE_USER_ANSWERS'])
        
    async def table_filling(self):
        """ Функция для заполнения таблиц значениями. """

        await self.pool.execute(INSERT_QUERIES['INSERT_INTO_QUESTIONS'])
        await self.pool.execute(INSERT_QUERIES['INSERT_INTO_ANSWERS'])

    async def add_user(
        self, 
        user_id: int, 
        username: str, 
        first_name: str, 
        last_name: str
    ) -> None:
        await self.pool.execute(
            INSERT_QUERIES['ADD_USER'], 
            user_id, 
            username, 
            first_name, 
            last_name
        )

    async def add_user_answer(
        self, 
        user_id: int, 
        question_id: int, 
        answer_id: int, 
        is_correct_answer: True | False
    ) -> None:
        await self.pool.execute(
            INSERT_QUERIES['ADD_USER_ANSWER'], 
            user_id, 
            question_id, 
            answer_id, 
            is_correct_answer
        )
