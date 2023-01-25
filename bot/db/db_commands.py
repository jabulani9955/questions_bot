import os

import dotenv
import psycopg2
import pandas as pd


async def get_from_db(query):
    try:
        connection = psycopg2.connect(
            host='localhost',
            user=os.getenv('db_user'),
            password=os.getenv('db_pass'),
            database =os.getenv('db_name')
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
    except Exception as e:
        print(f"[INFO] Error while working PostgreSQL", e)
    finally:
        if connection:
            connection.close()
            print(f"[INFO] PstgreSQL connection closed")


# class DataBase:
#     async def get_question(self):
#         with self.connection.cursor() as cursor:
#             cursor.execute("SELECT * FROM `questions`")
#             result = cursor.fetchone()
        
#         # df = pd.DataFrame(result)
#         return await result
