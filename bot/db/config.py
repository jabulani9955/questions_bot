import os

from dotenv import load_dotenv


load_dotenv()

QUERIES = {
    "GET_ALL_QUESTIONS": "SELECT * FROM questions;",
    "GET_USER": "SELECT * FROM users;",
    "GET_ANSWERS": "SELECT * FROM answers",
    "INSERT_INTO_QUESTIONS": """
        INSERT INTO questions VALUES (
            'Какой сегодня день?', 'Четверг'
        );
    """,
    "INSERT_INTO_ANSWERS": "INSERT INTO...",
    "INSERT_INTO_USERS": "INSERT INTO...",
    "CREATE_ANSWERS": """
        CREATE TABLE answers (
            answer_id integer not null,
            answered_by_id integer not null,
            answer_text VARCHAR(60) not null,
            foreign key (answer_id) references questions(id),
            foreign key (answered_by_id) references users(user_id)
        );
    """,
    "CREATE_USERS": """
        create table users (
            user_id integer primary key,
            name varchar(40) not null
        );
    """
}

DB_PARAMS = {
    "host": "localhost",
    "user": os.getenv("db_user"),
    "password": os.getenv("db_pass"),
    "database": os.getenv("db_name")
}
