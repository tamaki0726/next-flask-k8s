# app/port/user_repository.py
from abc import ABC, abstractmethod
from app.domain.user import User

class UserRepository(ABC):
    @abstractmethod
    def create(self, user: User):
        pass

    @abstractmethod
    def all_read(self):
        pass

    @abstractmethod
    def read(self, user_id):
        pass

    @abstractmethod
    def update(self, user_id, user: User):
        pass

    @abstractmethod
    def delete(self, user_id):
        pass
