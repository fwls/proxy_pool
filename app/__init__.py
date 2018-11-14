import redis
import config

pool= redis.ConnectionPool(host=config.redis_host, port=config.redis_port, decode_responses=True)
r=redis.Redis(connection_pool=pool)