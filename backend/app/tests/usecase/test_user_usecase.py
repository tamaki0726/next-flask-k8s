import unittest
from unittest.mock import MagicMock
from app.usecase.user_usecase import UserUseCase
from app.domain.user import User

class TestUserUseCase(unittest.TestCase):
    def setUp(self):
        self.mock_repository = MagicMock()
        self.usecase = UserUseCase(user_repository=self.mock_repository)

    def test_create_user(self):
        user_id = self.usecase.create_user("Alice", "alice@example.com")
        self.mock_repository.create.assert_called_once()
        self.assertEqual(self.mock_repository.create.call_args[0][0].name, "Alice")
        self.assertEqual(self.mock_repository.create.call_args[0][0].email, "alice@example.com")

    def test_get_users(self):
        self.usecase.get_users()
        self.mock_repository.all_read.assert_called_once()

    def test_get_user(self):
        user_id = "12345"
        self.usecase.get_user(user_id)
        self.mock_repository.read.assert_called_once_with(user_id)

    def test_update_user(self):
        user_id = "12345"
        self.usecase.update_user(user_id, "Bob", "bob@example.com")

        # 呼び出された引数を取得
        called_args = self.mock_repository.update.call_args[0]
        user = called_args[1]

        # 属性の比較
        self.assertEqual(called_args[0], user_id)
        self.assertEqual(user.name, "Bob")
        self.assertEqual(user.email, "bob@example.com")

    def test_delete_user(self):
        user_id = "12345"
        self.usecase.delete_user(user_id)
        self.mock_repository.delete.assert_called_once_with(user_id)

if __name__ == "__main__":
    unittest.main()
