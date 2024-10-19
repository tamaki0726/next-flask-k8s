# app/port/content_repository.py
from abc import ABC, abstractmethod
from app.domain.content import Content

class ContentRepository(ABC):
    @abstractmethod
    def all_read(self):
        pass

