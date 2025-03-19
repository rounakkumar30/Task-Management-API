import heapq
from .models import Task

class TaskPriorityQueue:
    def __init__(self):
        self.queue = []

    def add_task(self, task: Task):
        heapq.heappush(self.queue, (self.get_priority(task.priority), task.created_at, task))

    def get_priority(self, priority):
        return {"high": 1, "medium": 2, "low": 3}.get(priority, 3)

    def fetch_task(self):
        if self.queue:
            return heapq.heappop(self.queue)[2]
        return None
