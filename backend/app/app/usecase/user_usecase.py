# app/usecase/user_usecase.py
from app.port.user_repository import UserRepository
from app.domain.user import User

class UserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, name: str, email: str):
        user = User(name, email)
        return self.user_repository.create(user)
    
    def get_users(self):
        return self.user_repository.all_read()

    def get_user(self, user_id):
        return self.user_repository.read(user_id)

    def update_user(self, user_id, name: str, email: str):
        user = User(name, email)
        self.user_repository.update(user_id, user)

    def delete_user(self, user_id):
        self.user_repository.delete(user_id)
