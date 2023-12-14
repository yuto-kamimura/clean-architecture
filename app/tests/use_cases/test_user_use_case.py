from unittest import TestCase

from app.core.schemas.user import User
from app.interfaces.repositories.user_reposotiry import UserRepository
from app.core.use_cases.user_use_case import UserUseCases
from unittest import TestCase, mock
from app.core.schemas.user import User
from app.interfaces.repositories.user_reposotiry import UserRepository
from app.core.use_cases.user_use_case import UserUseCases


class UserRepositoryMock(UserRepository):
    def create(self, user: User) -> User:
        return user

    def get(self, user_id: int) -> User:
        user = User(id=user_id, name="test", password="test", email="test")
        return user
    
class UserUseCasesTest(TestCase):
    def setUp(self):
        self.user_repository = UserRepositoryMock()
        self.user_use_cases = UserUseCases(self.user_repository)

    def test_create_user(self):
        user = User(name="test", password="test", email="test")
        created_user = self.user_use_cases.create_user(user)
        self.assertEqual(created_user, user)
        # self.user_repository.create.assert_called_once_with(user)

    def test_get_user(self):
        user_id = 1
        user = User(id=user_id, name="test", password="test", email="test")
        self.user_repository.get.return_value = user
        retrieved_user = self.user_use_cases.get_user(user_id)
        self.assertEqual(retrieved_user, user)
        self.user_repository.get.assert_called_once_with(user_id)

    def test_authenticate_user(self):
        user = User(name="test", password="test", email="test")
        self.user_repository.get.return_value = user
        authenticated_user = self.user_use_cases.authenticate_user(user)
        self.assertEqual(authenticated_user, user)
        self.user_repository.get.assert_called_once_with(user.name)
        self.assertTrue(self.user_use_cases._verify_password.called)

    def test__verify_password(self):
        user = User(name="test", password="test", email="test")
        plain_user = User(name="test", password="test", email="test")
        self.assertTrue(self.user_use_cases._verify_password(user, plain_user))

    def test__encrypt_password(self):
        user = User(name="test", password="test", email="test")
        encrypted_password = self.user_use_cases._encrypt_password(user)
        self.assertTrue(encrypted_password)

