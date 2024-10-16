# app/port/user_repository.py
from abc import ABC, abstractmethod
from app.domain.cache import Cache

class CacheRepository(ABC):
    @abstractmethod
    def create(self, cache: Cache):
        pass

    @abstractmethod
    def all_read(self):
        pass

    @abstractmethod
    def read(self, key):
        pass
