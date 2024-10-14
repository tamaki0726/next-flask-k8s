import unittest
from app.domain.user import User

class TestUser(unittest.TestCase):
    def test_to_dict(self):
        user = User(name="John Doe", email="john@example.com")
        expected_dict = {"name": "John Doe", "email": "john@example.com"}
        self.assertEqual(user.to_dict(), expected_dict)

if __name__ == "__main__":
    unittest.main()
