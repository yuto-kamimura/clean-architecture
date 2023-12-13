from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class WordModel(Base):
    __tablename__ = "words"
    id = Column(Integer, primary_key=True, index=True, autoincrement="auto")
    english = Column(String, nullable=False)
    japanese = Column(String, nullable=False)
    difficulty = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=False)
