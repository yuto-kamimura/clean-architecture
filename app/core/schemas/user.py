from pydantic import BaseModel
import datetime


class User(BaseModel):
    id: int
    name: str
    password: str
    email: str
    updated_at: datetime.datetime
