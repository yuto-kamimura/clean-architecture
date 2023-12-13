from app.core.schemas.word import Word
from app.interfaces.repositories.word_repository import WordRepository
from app.interfaces.usecases.word_usecase import WordUseCases

class WordUseCases(WordUseCases):
    def __init__(self, word_repository: WordRepository):
        self.word_repository = word_repository

    def create_word(self, word: Word):
        return self.word_repository.create(word)

    def get_word(self, word_id: int):
        return self.word_repository.get(word_id)
