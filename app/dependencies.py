import redis
import json

redis_client = redis.Redis(host="localhost", port=6379, db=0)

def get_cached_tasks():
    cached_data = redis_client.get("tasks")
    if cached_data:
        return json.loads(cached_data)
    return None

def set_cached_tasks(tasks):
    redis_client.set("tasks", json.dumps([task.__dict__ for task in tasks]), ex=60)
