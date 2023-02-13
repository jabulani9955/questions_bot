from asyncio import AbstractEventLoop
import asyncpg

from bot.db.queries import CREATE_QUERIES, INSERT_QUERIES, GET_QUERIES


class DB:
    def __init__(
        self,
        dsn: str,
        loop: AbstractEventLoop,
        pool: asyncpg.pool.Pool
    ) -> None:
        self.dsn = dsn
        self.loop = loop
        self.pool = loop.run_until_complete(
            asyncpg.create_pool(
                dsn=dsn,
                loop=loop
            )
        )
    async def get_tests_list(self) -> list[asyncpg.Record]:
        return await self.pool.fetch(GET_QUERIES['GET_TESTS'])

    async def get_first_question_id(self, test_id: int) -> int:
        return await self.pool.fetchval(GET_QUERIES['GET_FIRST_QUESTION_ID'], test_id)

    async def get_correct_answer(self, test_id: int, question_num: int) -> asyncpg.Record:
        return await self.pool.fetch(GET_QUERIES['GET_CORRECT_ANSWER'], test_id, question_num)

    async def get_questions_num(self, test_id: int) -> int:
        return await self.pool.fetchval(GET_QUERIES['GET_NUM_QUESTIONS'], test_id)

    async def get_question_by_id(self, test_id: int, question_num: int) -> list[asyncpg.Record]:
        return await self.pool.fetch(GET_QUERIES['GET_QUESTION_BY_ID'], test_id, question_num)

    async def is_user_exist(self, user_id: int):
        return await self.pool.fetchrow(GET_QUERIES['GET_USER_BY_ID'], user_id)

    async def initial_creation(self):
        """ Функция для первоначального создания таблиц. """
        
        await self.pool.execute(CREATE_QUERIES['CREATE_TESTS'])        
        await self.pool.execute(CREATE_QUERIES['CREATE_USERS'])
        await self.pool.execute(CREATE_QUERIES['CREATE_QUESTIONS'])
        await self.pool.execute(CREATE_QUERIES['CREATE_ANSWERS'])
        await self.pool.execute(CREATE_QUERIES['CREATE_USER_ANSWERS'])

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
        test_id: int,
        question_num: int, 
        answer_id: int, 
        is_correct_answer: True | False
    ) -> None:
        await self.pool.execute(
            INSERT_QUERIES['ADD_USER_ANSWER'], 
            user_id, 
            test_id,
            question_num,
            answer_id, 
            is_correct_answer
        )
