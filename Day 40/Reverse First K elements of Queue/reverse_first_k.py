from collections import deque

class Solution:
    def modifyQueue(self, q, k):
       
        q = deque(q)
        temp = []
        i = 0
        
        while i<k:
            temp.append(q.popleft())
            i += 1
        
        while temp:
            q.append(temp.pop())
            
        i = 0
        while i<len(q) - k:
            ele = q.popleft()
            q.append(ele)
            i += 1
            
        return q