from fastapi import APIRouter, HTTPException
from app.core.use_cases.word_use_cases import WordUseCases
from app.core.schemas.word import Word
from app.core.repositories.word_repository import SQLAlchemyWordRepository
from app.db.database import PostgreseDB

router = APIRouter()

# リポジトリの実装を注入
word_repository = SQLAlchemyWordRepository(PostgreseDB())
word_usecase = WordUseCases(word_repository)


@router.post("/words/")
async def create_word_endpoint(word: Word):
    try:
        created_word = word_usecase.create_word(word, word_repository)
        return created_word
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/words/{word_id}")
async def get_word_endpoint(word_id: int):
    try:
        word = word_usecase.get_word(word_id, word_repository)
        if word is None:
            raise HTTPException(status_code=404, detail="Word not found")
        return word
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
