import redis

class RedisService:

    def __init__(self):
        self.redis_client = redis.StrictRedis(host='172.206.234.253', port=6379, db=0)

    def set(self, key, value, ex=None):
        self.redis_client.set(key, value, ex=ex)

    def get(self, key):
        return self.redis_client.get(key)
