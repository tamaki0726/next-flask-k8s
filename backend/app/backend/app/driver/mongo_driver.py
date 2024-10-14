# app/driver/mongo_driver.py
from pymongo import MongoClient

class MongoDriver:
    def __init__(self, mongo_uri):
        self.client = MongoClient(mongo_uri)
        self.db = self.client['mydatabase']

    def get_collection(self, collection_name):
        return self.db[collection_name]
