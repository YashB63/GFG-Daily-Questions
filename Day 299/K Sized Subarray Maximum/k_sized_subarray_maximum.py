from collections import deque

class Solution:
    def max_of_subarrays(self,k,arr):
        res = []
        q = deque()
        for i in range(len(arr)):
            if len(q) and q[0] <= i - k:
                q.popleft()
            while len(q) and arr[q[-1]] < arr[i]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                res.append(arr[q[0]])
        
        return res