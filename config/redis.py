import os
import redis
from dotenv import load_dotenv

load_dotenv()

redis_pool = redis.ConnectionPool(host=os.environ.get('APP_REDIS_HOST'),
                                  port=6379,
                                  db=0,
                                  password=os.environ.get('APP_REDIS_PASSWORD'))

redis_client = redis.Redis(connection_pool=redis_pool)
