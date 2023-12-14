from app.core.models.user_model import UserModel
from app.core.schemas.user import User
from app.interfaces.repositories.user_reposotiry import UserRepository
from app.db.database import DBInterface


class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, db: DBInterface):
        self._session = db.db_session()

    def create(self, user: User) -> User:
        db_user = UserModel(
            name=user.name,
            password=user.password,
            email=user.email,
            updated_at=user.updated_at,
        )
        self._session.add(db_user)
        self._session.commit()
        self._session.refresh(db_user)
        self._session.close()
        return User(
            id=db_user.id,
            name=db_user.name,
            password=db_user.password,
            email=db_user.email,
            updated_at=db_user.updated_at,
        )

    def get(self, user_id: int) -> User:
        db_user = self._session.query(UserModel).filter(UserModel.id == user_id).first()
        self._session.close()
        if db_user:
            return User(
                id=db_user.id,
                name=db_user.name,
                password=db_user.password,
                updated_at=db_user.updated_at,
            )
        return None
