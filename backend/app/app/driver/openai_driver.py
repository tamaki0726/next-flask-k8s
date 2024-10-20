# app/driver/mongo_driver.py
from openai import OpenAI

class OpenAiDriver:
    def __init__(self, openai_api_key):
        self.client = OpenAI(
            organization=openai_api_key,
        )
    
    def chat(self, prompt):
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response
    
    def close(self):
        self.client.close()