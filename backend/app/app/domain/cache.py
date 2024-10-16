# app/domain/cache.py
class Cache:
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
