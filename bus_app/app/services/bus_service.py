import json
from app.cache.redis_cache import cache_bus_info, get_cached_bus_info
from app.services.kakao_service import get_bus_location

def get_bus_info(bus_id):
    cached_info = get_cached_bus_info(bus_id)
    if cached_info:
        return json.loads(cached_info)
    
    bus_info = get_bus_location(bus_id)
    cache_bus_info(bus_id, json.dumps(bus_info))
    return bus_info
