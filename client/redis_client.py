import redis
import json
import os

REDIS_HOST = os.getenv('REDIS_SERVER', 'localhost')


class RedisClient:
    def __init__(self):
        self.redis = redis.Redis(host=REDIS_HOST, port=6379, db=1)

    def set(self, key, value):
        self.redis.set(key, json.dumps(value))

    def get(self, key):
        if not self.redis.exists(key):
            return None
        return json.loads(self.redis.get(key))
