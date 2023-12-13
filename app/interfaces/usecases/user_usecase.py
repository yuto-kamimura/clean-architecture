from abc import ABC, abstractmethod
from app.core.schemas.user import User

class UserUseCases(ABC):
    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> User:
        pass

    @abstractmethod
    def authenticate_user(self, plain_user: User) -> User:
        pass