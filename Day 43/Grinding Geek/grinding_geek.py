from typing import List

class Solution:
    def max_courses(self, n : int, total : int, cost : List[int]) -> int:
        
        x = [0 for _ in range(total + 1)]
        for c in reversed(cost):
            for t in range(total, c-1, -1):
                x[t] = max(x[t], x[t - (c + 9)//10] + 1)
        
        return x[total]