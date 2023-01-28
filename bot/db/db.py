import os

import psycopg2

from .config import DB_PARAMS, CREATE_QUERIES, INSERT_QUERIES


async def connect_to_db():
    try:
        connection = psycopg2.connect(**DB_PARAMS)
        # connection.autocommit = True
        print("Connection successful")
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    return connection


def get_all_questions(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM questions"
    cursor.execute(query)
    all_questions = cursor.fetchall()
    return all_questions


async def run_query(query: str, to_get=True):
    try:
        connection = psycopg2.connect(**DB_PARAMS)
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(query)

            if to_get:
                return cursor.fetchall()

    except Exception as e:
        print(f"[INFO] Error while working PostgreSQL", e)
    finally:
        if connection:
            connection.close()


def initial_creation():
    """ Функция для первоначального создания таблиц. """

    try:
        run_query(CREATE_QUERIES['CREATE_USERS'], to_get=False)
        run_query(CREATE_QUERIES['CREATE_QUESTIONS'], to_get=False)
        run_query(CREATE_QUERIES['CREATE_ANSWERS'], to_get=False)
    except Exception as e:
        print(f"Ошибка!!!\n{e}")
        

def table_filling():
    """ Функция для заполнения таблиц значениями. """

    try:
        run_query(INSERT_QUERIES['INSERT_INTO_USERS'], to_get=False)
        run_query(INSERT_QUERIES['INSERT_INTO_QUESTIONS'], to_get=False)
        run_query(INSERT_QUERIES['INSERT_INTO_ANSWERS'], to_get=False)
    except Exception as e:
        print(f"Ошибка!!!\n{e}")     


if __name__ == "__main__":
    # initial_creation() # Первоначальное создание таблиц.
    table_filling() # Заполнение таблиц значениями.