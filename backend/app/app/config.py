# app/config.py
import os
from dotenv import load_dotenv

class Config:
    load_dotenv()

    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://root:root@localhost:27017/mydatabase?authSource=admin')
    REDIS_URI = os.getenv('REDIS_URI', 'localhost')
    OPENAI_API_KEY = os.getenv('OPEN_API_KEY')