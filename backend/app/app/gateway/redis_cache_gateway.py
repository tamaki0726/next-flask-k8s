# app/gateway/mongo_user_gateway.py
from app.port.cache_repository import CacheRepository
from app.domain.cache import Cache
from app.driver.redis_driver import RedisDriver

class RedisCacheGateway(CacheRepository):
    def __init__(self, redis_uri):
        self.redis_driver = RedisDriver(redis_uri)
        self.client = self.redis_driver.get_client()

    def create(self, cache: Cache):
        result = self.client.set(cache.key, cache.value)
        return str(result)
    
    def all_read(self):
        keys = self.client.keys('*')
        return {key.decode('utf-8'): self.client.get(key).decode('utf-8') for key in keys}

    def read(self, key):
        value = self.client.get(key)
        return value.decode('utf-8')
    
    def close(self):
        self.redis_driver.close()
