from abc import ABC, abstractmethod
from app.core.schemas.word import Word


class WordRepository(ABC):
    @abstractmethod
    def create(self, item: Word) -> Word:
        pass

    @abstractmethod
    def get(self, item_id: int) -> Word:
        pass
