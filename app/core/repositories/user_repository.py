from app.core.models.user_model import UserModel
from app.core.schemas.user import User
from app.interfaces.user_reposotiry import UserRepository
from app.db.database import DBInterface


class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, db: DBInterface):
        self.session = db.db_session()

    def create(self, user: User) -> User:
        db_user = UserModel(
            name=user.name, password=user.password, created_at=user.created_at
        )
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        self.session.close()
        return User(
            id=db_user.id,
            name=db_user.name,
            password=db_user.password,
            created_at=db_user.created_at,
        )

    def get(self, user_id: int) -> User:
        db_user = self.session.query(UserModel).filter(UserModel.id == user_id).first()
        self.session.close()
        if db_user:
            return User(
                id=db_user.id,
                name=db_user.name,
                password=db_user.password,
                created_at=db_user.created_at,
            )
        return None
