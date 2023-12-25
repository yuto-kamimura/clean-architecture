from abc import ABC, abstractmethod
from app.core.schemas.user import User


class UserRepository(ABC):
    @abstractmethod
    def create(self, item: User) -> User:
        pass

    @abstractmethod
    def get(self, item_id: int) -> User:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> User:
        pass