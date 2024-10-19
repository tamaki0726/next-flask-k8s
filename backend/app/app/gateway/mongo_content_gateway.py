# app/gateway/mongo_user_gateway.py
from bson.objectid import ObjectId
from app.port.content_repository import ContentRepository
from app.driver.mongo_driver import MongoDriver

class MongoContentGateway(ContentRepository):
    def __init__(self, mongo_uri):
        self.mongo_driver = MongoDriver(mongo_uri)
        self.collection = self.mongo_driver.get_collection('contents')

    def all_read(self):
        return self.collection.find()
    
    def close(self):
        self.mongo_driver.close()
