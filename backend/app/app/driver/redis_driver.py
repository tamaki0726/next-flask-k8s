import redis

class RedisDriver:
    def __init__(self, redis_uri, redis_port=6379, redis_db=0):
        self.client = redis.StrictRedis(host=redis_uri, port=redis_port, db=redis_db)

    def get_client(self):
        return self.client
    
    def close(self):
        self.client.close()