# app/port/content_repository.py
from abc import ABC, abstractmethod
from app.domain.content import Content

class ContentOpenAiRepository(ABC):
    @abstractmethod
    def extract(self, prompt):
        pass

