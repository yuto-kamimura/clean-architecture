import bcrypt

from app.core.schemas.user import User
from app.interfaces.user_reposotiry import UserRepository


class UserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user: User):
        user.password = self._encrypt_password(user, 12)
        return self.user_repository.create(user)

    def get_user(self, user_id: int):
        return self.user_repository.get(user_id)

    def authenticate_user(self, plain_user: User) -> User:
        user = self.user_repository.get(plain_user.id)

        if user and self._verify_password(user, plain_user):
            return user
        else:
            return None

    def _verify_password(self, user: User, plain_user: User) -> bool:
        if bcrypt.checkpw(plain_user.password.encode(), user.password.encode()):
            return True
        else:
            return False

    def _encrypt_password(self, user: User, rounds=12) -> str:
        return bcrypt.hashpw(user.password.encode(), bcrypt.gensalt(rounds)).decode()
