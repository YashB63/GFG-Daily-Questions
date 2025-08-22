from typing import List
from collections import deque
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        ans = [-1 for i in range(100001)]
    
        mod = 100000
    
        q = deque()
        
        q.append(start % mod)
    
        ans[start] = 0
    
        while (len(q) > 0):
    
            top = q.popleft()
    
            if (top == end):
                return ans[end]
    
            for i in range(len(arr)):
                pushed = top * arr[i]
                pushed = pushed % mod
    
                if (ans[pushed] == -1):
                    ans[pushed] = ans[top] + 1
                    q.append(pushed)
                
        return -1