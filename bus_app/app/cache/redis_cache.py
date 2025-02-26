import redis
from flask import current_app

redis_client = None

def get_redis_client():
    global redis_client
    if redis_client is None:
        redis_client = redis.Redis(
            host=current_app.config['REDIS_HOST'],
            port=current_app.config['REDIS_PORT'],
            db=current_app.config['REDIS_DB']
        )
    return redis_client

def cache_bus_info(bus_id, bus_info, expire_time=300):
    client = get_redis_client()
    client.setex(f"bus:{bus_id}", expire_time, bus_info)

def get_cached_bus_info(bus_id):
    client = get_redis_client()
    return client.get(f"bus:{bus_id}")
