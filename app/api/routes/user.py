from fastapi import APIRouter, HTTPException
from app.core.use_cases.user_use_cases import UserUseCase
from app.core.schemas.user import User
from app.core.repositories.user_repository import SQLAlchemyUserRepository
from app.db.database import PostgreseDB

router = APIRouter()

# リポジトリの実装を注入
user_repository = SQLAlchemyUserRepository(PostgreseDB())
user_usecase = UserUseCase(user_repository)


@router.post("/users/", status_code=201)
def create_user_endpoint(user: User):
    try:
        created_user = user_usecase.create_user(user)
        return created_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/users/{user_id}")
def get_user_endpoint(user_id: int):
    try:
        user = user_usecase.get_user(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/login/", status_code=200)
def post_user_endpoint(user: User):
    try:
        login_user = user_usecase.authenticate_user(user)
        if login_user is None:
            return HTTPException(status_code=403, detail="Login failed")
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
