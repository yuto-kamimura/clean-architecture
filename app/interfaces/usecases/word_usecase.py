from abc import ABC, abstractmethod
from app.core.schemas.word import Word

class WordUseCases(ABC):
    @abstractmethod
    def create_word(self, word: Word):
        pass

    @abstractmethod
    def get_word(self, word_id: int):
        pass