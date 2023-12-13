from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from abc import ABC, abstractmethod


class DBInterface(ABC):
    @abstractmethod
    def db_session() -> sessionmaker:
        pass


class PostgreseDB(DBInterface):
    def __init__(self) -> None:
        SQLALCHEMY_DATABASE_URL = (
            "postgresql://postgres:postgres@localhost:5432/postgres"
        )
        # SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@0.0.0.0:5432/fastapi_todo_app_development"

        engine = create_engine(
            SQLALCHEMY_DATABASE_URL,
            echo=False,
        )
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def db_session(self) -> sessionmaker:
        return self.SessionLocal()


class MariaDB(DBInterface):
    def __init__(self) -> None:
        super().__init__()

    def db_session() -> sessionmaker:
        pass


# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"
# # SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@0.0.0.0:5432/fastapi_todo_app_development"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,
#     echo=False,
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# def db_session() -> sessionmaker:
#     return SessionLocal()
