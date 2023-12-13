from pydantic import BaseModel
import datetime


class Word(BaseModel):
    id: int
    english: str
    japanese: str
    difficulty: int
    description: str
    updated_at: datetime.datetime
