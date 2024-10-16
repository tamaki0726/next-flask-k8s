# app/usecase/user_usecase.py
from app.port.cache_repository import CacheRepository
from app.domain.cache import Cache

class CacheUseCase:
    def __init__(self, cache_repository: CacheRepository):
        self.cache_repository = cache_repository

    def create_cache(self, key: str, value: str):
        cache = Cache(key, value)
        return self.cache_repository.create(cache)
    
    def get_caches(self):
        return self.cache_repository.all_read()

    def get_cache(self, key):
        return self.cache_repository.read(key)
