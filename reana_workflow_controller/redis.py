from reana_commons.config import REANA_INFRASTRUCTURE_COMPONENTS_HOSTNAMES

from redis import StrictRedis
from redis_cache import RedisCache

client = StrictRedis(host=REANA_INFRASTRUCTURE_COMPONENTS_HOSTNAMES["cache"], port=6379, decode_responses=True)
redis_cache = RedisCache(redis_client=client)
