from bson.objectid import ObjectId
from unittest import TestCase
from app.gateway.mongo_user_gateway import MongoUserGateway
from app.domain.user import User
from unittest.mock import MagicMock

class TestMongoUserGateway(TestCase):
    def setUp(self):
        self.gateway = MongoUserGateway('mongodb://username:password@localhost:27017')
        self.gateway.collection = MagicMock()

    def test_all_read(self):
        mock_users = [
            {"_id": ObjectId(), "name": "Alice", "email": "alice@example.com"},
            {"_id": ObjectId(), "name": "Bob", "email": "bob@example.com"},
        ]
        self.gateway.collection.find.return_value = mock_users
        
        users = self.gateway.all_read()
        
        # Userオブジェクトのリストを作成
        users = [User(name=user["name"], email=user["email"]) for user in users]

        self.gateway.collection.find.assert_called_once()
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].name, "Alice")
        self.assertEqual(users[1].name, "Bob")

    def test_create_user(self):
        user = User(name="Alice", email="alice@example.com")
        self.gateway.create(user)
        self.gateway.collection.insert_one.assert_called_once_with(user.to_dict())

    def test_delete_user(self):
        user = User(name="Alice", email="alice@example.com")
        self.gateway.create(user)
        user_id = str(ObjectId())  # 有効なIDを生成
        self.gateway.delete(user_id)
        self.gateway.collection.delete_one.assert_called_once_with({"_id": ObjectId(user_id)})

    def test_read_user(self):
        user = User(name="Alice", email="alice@example.com")
        self.gateway.create(user)
        user_id = str(ObjectId())  # 有効なIDを生成
        self.gateway.read(user_id)
        self.gateway.collection.find_one.assert_called_once_with({"_id": ObjectId(user_id)})

    def test_update_user(self):
        user = User(name="Alice", email="alice@example.com")
        self.gateway.create(user)
        user_id = str(ObjectId())  # 有効なIDを生成
        self.gateway.update(user_id, user)
        self.gateway.collection.update_one.assert_called_once_with({"_id": ObjectId(user_id)}, {"$set": user.to_dict()})
    
    def tearDown(self):
        self.gateway.close()