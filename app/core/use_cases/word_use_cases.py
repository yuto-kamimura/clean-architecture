from app.core.schemas.word import Word
from app.interfaces.word_repository import WordRepository


class WordUseCase:
    def __init__(self, word_repository: WordRepository):
        self.word_repository = word_repository

    def create_word(self, word: Word):
        return self.word_repository.create(word)

    def get_word(self, word_id: int):
        return self.word_repository.get(word_id)
