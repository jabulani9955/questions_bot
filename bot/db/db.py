import os

import psycopg2

from config import DB_PARAMS, QUERIES


def run_query(query: str, to_get=True):
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


if __name__ == "__main__":
    # run_query(QUERIES['CREATE_USERS'], to_get=False)
    run_query(QUERIES['CREATE_ANSWERS'], to_get=False)