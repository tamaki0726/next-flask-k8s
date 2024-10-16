# app/config.py
import os

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://root:root@localhost:27017/mydatabase?authSource=admin')
    REDIS_URI = os.getenv('REDIS_URI', 'localhost')
