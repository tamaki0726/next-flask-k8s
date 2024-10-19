# app/domain/content.py
class Content:
    def __init__(self, name: str, userName: str, date: str):
        self.name = name
        self.userName = userName
        self.date = date