CREATE_QUERIES = {
    "CREATE_TESTS": """
        CREATE TABLE IF NOT EXISTS tests (
            id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL
        );
    """,
    "CREATE_QUESTIONS": """
        CREATE TABLE IF NOT EXISTS questions (
            id SERIAL PRIMARY KEY,
            test_id INTEGER REFERENCES tests(id) NOT NULL,
            question VARCHAR NOT NULL,
            created_at TIMESTAMP NOT NULL
        );
    """,
    "CREATE_ANSWERS": """
        CREATE TABLE IF NOT EXISTS answers (
            id SERIAL PRIMARY KEY,
            test_id INTEGER REFERENCES tests(id) NOT NULL,
            question_id INTEGER REFERENCES questions(id) NOT NULL,
            answer VARCHAR NOT NULL,
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
            test_id INTEGER REFERENCES tests(id) NOT NULL,
            question_id INTEGER REFERENCES questions(id),
            answer_id INTEGER REFERENCES answers(id) NOT NULL,
            answer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            is_correct_answer BOOLEAN NOT NULL
        );
    """
}
INSERT_QUERIES = {
    "ADD_USER": """
        INSERT INTO users (
            user_id,
            username,
            first_name,
            last_name,
            first_login_time
        ) VALUES (
            $1,
            $2,
            $3,
            $4,
            NOW()
        );
    """,
    "ADD_USER_ANSWER": """
        INSERT INTO user_answers (
            user_id, test_id, question_id, answer_id, answer_date, is_correct_answer) VALUES (
            $1, $2, $3, $4, NOW(), $5);
    """
}
GET_QUERIES = {
    "GET_TESTS": """
        SELECT * FROM tests;
    """,
    "GET_CORRECT_ANSWER": """
        SELECT
            answers.answer,
            answers.id as answer_id
        FROM questions
        JOIN answers ON questions.id = answers.question_id
        WHERE questions.test_id = $1 AND questions.id = $2 and answers.is_correct = true
    """,
    "GET_NUM_QUESTIONS": """
        SELECT COUNT(DISTINCT questions.id) as n_questions
        FROM questions
        WHERE questions.test_id = $1;
    """,
    "GET_QUESTION_BY_ID": """
        SELECT
            questions.question, 
            answers.id as answer_id, 
            answers.answer
        FROM questions JOIN answers ON questions.id = answers.question_id
        WHERE questions.test_id = $1 AND question_id = $2
    """,
    "GET_USER_BY_ID": """
        SELECT * FROM users WHERE user_id = $1;
    """
}
