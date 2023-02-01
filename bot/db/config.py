import os

from dotenv import load_dotenv


load_dotenv()

DB_PARAMS = {
    "host": "localhost",
    "user": os.getenv("db_user"),
    "password": os.getenv("db_pass"),
    # "database": os.getenv("db_name")
    "database": os.getenv("db_name_example")    
}

CREATE_QUERIES = {
    "CREATE_QUESTIONS": """
        CREATE TABLE IF NOT EXISTS questions (
            id SERIAL PRIMARY KEY,
            test_id INTEGER NOT NULL,
            question VARCHAR(255) NOT NULL,
            created_at TIMESTAMP NOT NULL
        );
    """,
    "CREATE_ANSWERS": """
        CREATE TABLE IF NOT EXISTS answers (
            id SERIAL PRIMARY KEY,
            test_id INTEGER REFERENCES questions(test_id) NOT NULL,
            question_id INTEGER REFERENCES questions(id) NOT NULL,
            answer VARCHAR(255) NOT NULL,
            created_at TIMESTAMP NOT NULL,
            is_correct BOOLEAN NOT NULL DEFAULT false
        );
    """,
    "CREATE_USERS": """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            user_id BIGINT NOT NULL,
            username VARCHAR,
            first_name VARCHAR,
            last_name VARCHAR,
            first_login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
        );
    """,
    "CREATE_USER_ANSWERS": """
        CREATE TABLE IF NOT EXISTS user_answers (
            id SERIAL PRIMARY KEY,
            user_id BIGINT NOT NULL,
            test_id INTEGER REFERENCES questions(test_id) NOT NULL,
            question_id INTEGER REFERENCES questions(id),
            answer_id INTEGER REFERENCES answers(id) NOT NULL,
            answer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            is_correct_answer BOOLEAN NOT NULL
        )
    """
}
INSERT_QUERIES = {
    "INSERT_INTO_QUESTIONS": """
        INSERT INTO questions (question, created_at) VALUES
            ('What is the capital of France?', NOW()),
            ('What is the largest planet in our solar system?', NOW()),
            ('What is the most populous country in the world?', NOW()),
            ('На каком озере произошло Ледовое побоище?', NOW()),
            ('Какое название носит основной отчёт у бухгалтеров?', NOW()),
            ('Что изучает Селенолог?', NOW());
    """,
    "INSERT_INTO_ANSWERS": """
        INSERT INTO answers (question_id, answer, created_at, is_correct) VALUES
            (1, 'Paris', NOW(), true),
            (1, 'Rome', NOW(), false),
            (1, 'Moscow', NOW(), false),
            (1, 'Madrid', NOW(), false),
            (2, 'Saturn', NOW(), false),
            (2, 'Jupiter', NOW(), true),
            (2, 'Mars', NOW(), false),
            (2, 'Venera', NOW(), false),
            (3, 'China', NOW(), false),
            (3, 'India', NOW(), true),
            (3, 'Russia', NOW(), false),
            (3, 'USA', NOW(), false),
            (4, 'Ладожское', NOW(), false),
            (4, 'Байкал', NOW(), false),
            (4, 'Чудское', NOW(), true),
            (4, 'Паравани', NOW(), false),
            (5, 'Сумма', NOW(), false),
            (5, 'Баланс', NOW(), true),
            (5, 'Транзакция', NOW(), false),
            (5, 'Счёт', NOW(), false),
            (6, 'Деревья', NOW(), false),
            (6, 'Животных', NOW(), false),
            (6, 'Луну', NOW(), true),
            (6, 'Грибы', NOW(), false);
    """,
    "ADD_USER": """
        INSERT INTO users (
            user_id,
            username,
            first_name,
            last_name,
            first_login_time
        ) VALUES (
            %s,
            %s,
            %s,
            %s,
            NOW()
        );
    """,
    "ADD_USER_ANSWER": """
        INSERT INTO user_answers (
            user_id, question_id, answer_id, answer_date, is_correct_answer) VALUES (
            %s, %s, %s, NOW(), %s);
    """
}
GET_QUERIES = {
    "GET_ALL_QUESTIONS": """
        SELECT questions.question 
        FROM questions;
    """,
    "GET_QUESTION_AND_ANSWER": """
        SELECT 
            questions.id as question_id, 
            questions.question, 
            answers.id as answer_id, 
            answers.answer, 
            answers.is_correct
        FROM questions
        JOIN answers ON questions.id = answers.question_id
    """,
    "GET_ALL_ANSWERS": """
        SELECT id, question_id, answer, is_correct
        FROM answers
    """,
    "GET_CORRECT_ANSWER": """
        SELECT
            answers.answer,
            answers.id as answer_id
        FROM questions
        JOIN answers ON questions.id = answers.question_id
        WHERE questions.id = %s and answers.is_correct = true
    """,
    "GET_NUM_QUESTIONS": """
        SELECT COUNT(DISTINCT questions.id) as n_questions
        FROM questions;
    """,
    "GET_QUESTION_BY_ID": """
        SELECT 
            questions.id as question_id, 
            questions.question, 
            answers.id as answer_id, 
            answers.answer, 
            answers.is_correct
        FROM questions
        JOIN answers ON questions.id = answers.question_id
        WHERE question_id = %s
    """,
    "GET_USER_BY_ID": """
        SELECT * FROM users WHERE user_id = %s;
    """
}

