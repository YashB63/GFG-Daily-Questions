from collections import Counter, deque
from heapq import heappush, heappop, heapify

class Solution:
    def leastInterval(self, N, K, tasks):
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())
        
        max_freq_tasks = sum(1 for task in task_counts.values() if task == max_freq)
        part_count = max_freq - 1
        part_length = K + 1
        empty_slots = part_count * part_length + max_freq_tasks
        
        return max(empty_slots, len(tasks))