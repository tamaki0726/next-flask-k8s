# app/usecase/content_usecase.py
from app.port.content_repository import ContentRepository
from app.domain.content import Content

class ContentUseCase:
    def __init__(self, content_repository: ContentRepository):
        self.content_repository = content_repository
    
    def get_contents(self):
        return self.content_repository.all_read()
