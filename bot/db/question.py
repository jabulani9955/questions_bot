from sqlalchemy import Column, Integer, VARCHAR, select, BigInteger, Enum, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, selectinload
from sqlalchemy.exc import ProgrammingError

from .base import BaseModel


class Question(BaseModel):
    __tablename__ = 'questions'

    _id = Column(Integer, unique=True, nullable=False, primary_key=True)
    question_text = Column(VARCHAR(32), unique=False, nullable=False)
    correct_answer_text = Column(VARCHAR(32), unique=False, nullable=False)


class Answer(BaseModel):
    __tablename__ = 'answers'

    _id = Column(Integer, unique=True, nullable=False, primary_key=True)
    question_id = Column(Integer, ForeignKey("questions._id"), nullable=False)
    

async def get_question(question_id: int, session_maker: sessionmaker) -> Question:
    async with session_maker() as session:
        async with session.begin():
            return (
                await session.execute(select(Question).where(Question._id == question_id))
            ).scalars().unique().one_or_none()
