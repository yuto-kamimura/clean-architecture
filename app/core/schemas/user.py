from pydantic import BaseModel
import datetime


class User(BaseModel):
    id: int
    name: str
    password: str
    created_at: datetime.datetime
