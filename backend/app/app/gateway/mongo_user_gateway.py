# app/gateway/mongo_user_gateway.py
from bson.objectid import ObjectId
from app.port.user_repository import UserRepository
from app.domain.user import User
from app.driver.mongo_driver import MongoDriver

class MongoUserGateway(UserRepository):
    def __init__(self, mongo_uri):
        self.mongo_driver = MongoDriver(mongo_uri)
        self.collection = self.mongo_driver.get_collection('users')

    def create(self, user: User):
        result = self.collection.insert_one(user.to_dict())
        return str(result.inserted_id)
    
    def all_read(self):
        return self.collection.find()

    def read(self, user_id):
        return self.collection.find_one({"_id": ObjectId(user_id)})

    def update(self, user_id, user: User):
        self.collection.update_one({"_id": ObjectId(user_id)}, {"$set": user.to_dict()})

    def delete(self, user_id):
        self.collection.delete_one({"_id": ObjectId(user_id)})
    
    def close(self):
        self.mongo_driver.close()
