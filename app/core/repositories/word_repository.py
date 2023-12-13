from app.core.models.word_model import WordModel
from app.core.schemas.word import Word
from app.interfaces.repositories.word_repository import WordRepository
from app.db.database import DBInterface


class SQLAlchemyWordRepository(WordRepository):
    def __init__(self, db: DBInterface):
        self.session = db.db_session()

    def create(self, word: Word) -> Word:
        db_word = WordModel(
            english=word.english,
            japanese=word.japanese,
            difficulty=word.difficulty,
            description=word.description,
            updated_at=word.updated_at,
        )
        self.session.add(db_word)
        self.session.commit()
        self.session.refresh(db_word)
        self.session.close()
        return Word(
            id=db_word.id,
            english=db_word.english,
            japanese=db_word.japanese,
            difficulty=db_word.difficulty,
            description=db_word.description,
            updated_at=db_word.updated_at,
        )

    def get(self, word_id: int) -> Word:
        db_word = self.session.query(WordModel).filter(WordModel.id == word_id).first()
        self.session.close()
        if db_word:
            return Word(
                id=db_word.id,
                english=db_word.english,
                japanese=db_word.japanese,
                difficulty=db_word.difficulty,
                description=db_word.description,
                updated_at=db_word.updated_at,
            )
        return None
