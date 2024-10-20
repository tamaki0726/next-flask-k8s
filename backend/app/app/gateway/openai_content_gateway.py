# app/gateway/mongo_user_gateway.py
from bson.objectid import ObjectId
from app.port.content_openai_repository import ContentOpenAiRepository
from app.driver.openai_driver import OpenAiDriver

class OpenAiContentGateway(ContentOpenAiRepository):
    def __init__(self, openai_api_key):
        self.openai_driver = OpenAiDriver(openai_api_key)

    def extract(self, prompt):
        completion = self.openai_driver.chat(prompt)
        return completion.choices[0].message.content
    
    def close(self):
        self.openai_driver.close()
