import os

import asyncio
import psycopg2
import pandas as pd

from .config import DB_PARAMS, CREATE_QUERIES, INSERT_QUERIES, GET_QUERIES


# class DataBase:
#     def __init__(self, DB_PARAMS) -> None:
#         try:
#             connection = psycopg2.connect(**DB_PARAMS)
#             connection.autocommit = True
#             # print("Connection successful")
#         except (Exception, psycopg2.Error) as error:
#             print("Error while connecting to PostgreSQL", error)


async def connect_to_db():
    try:
        connection = psycopg2.connect(**DB_PARAMS)
        connection.autocommit = True
        # print("Connection successful")
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    return connection


async def get_correct_answer(question_id: int):
    with await connect_to_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(GET_QUERIES['GET_CORRECT_ANSWER'], (question_id, ))
            return cursor.fetchone() 
    

async def get_questions_num():
    with await connect_to_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(GET_QUERIES['GET_NUM_QUESTIONS'])
            return int(cursor.fetchone()[0])


async def get_question_by_id(question_id: int):
    with await connect_to_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(GET_QUERIES['GET_QUESTION_BY_ID'], (question_id,))
            return cursor.fetchall()


async def run_query(query: str, to_get=True, to_df=False) -> list | pd.DataFrame | None:
    try:
        connection = await connect_to_db()

        with connection.cursor() as cursor:
            cursor.execute(query)

            if to_get:
                answers = cursor.fetchall()

                if to_df:
                    column_names = [i[0] for i in cursor.description]
                    df = pd.DataFrame(answers, columns=column_names)
                    return df

                return answers

    except Exception as e:
        print(f"[INFO] Error while working PostgreSQL", e)
    finally:
        if connection:
            connection.close()


async def add_user(user_id: int, username: str, first_name: str, last_name: str) -> None:
    with await connect_to_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(INSERT_QUERIES['ADD_USER'], (user_id, username, first_name, last_name))


async def add_user_answer(user_id: int, question_id: int, answer_id: int, is_correct_answer: True | False) -> None:
    with await connect_to_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(INSERT_QUERIES['ADD_USER_ANSWER'], (user_id, question_id, answer_id, is_correct_answer))


async def is_user_exist(user_id: int) -> None:
    with await connect_to_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(GET_QUERIES['GET_USER_BY_ID'], (user_id,))
            result = cursor.fetchall()
            return bool(len(result))

async def initial_creation():
    """ Функция для первоначального создания таблиц. """

    try:
        await run_query(CREATE_QUERIES['CREATE_USERS'], to_get=False)
        await run_query(CREATE_QUERIES['CREATE_QUESTIONS'], to_get=False)
        await run_query(CREATE_QUERIES['CREATE_ANSWERS'], to_get=False)
        await run_query(CREATE_QUERIES['CREATE_USER_ANSWERS'], to_get=False)
    except Exception as e:
        print(f"Ошибка!!!\n{e}")
        

async def table_filling():
    """ Функция для заполнения таблиц значениями. """

    try:
        # run_query(INSERT_QUERIES['INSERT_INTO_USERS'], to_get=False)
        await run_query(INSERT_QUERIES['INSERT_INTO_QUESTIONS'], to_get=False)
        await run_query(INSERT_QUERIES['INSERT_INTO_ANSWERS'], to_get=False)
    except Exception as e:
        print(f"Ошибка!!!\n{e}")     


async def main():
    # Первоначальное создание таблиц.
    await initial_creation()

    # Заполнение таблиц значениями.
    # await table_filling() 

if __name__ == "__main__":
    asyncio.run(main()) 
