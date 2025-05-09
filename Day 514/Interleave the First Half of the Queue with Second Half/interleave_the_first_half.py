from collections import deque

class Solution:
    def rearrangeQueue(self, q):
        if len(q) % 2== 1:
            q.pop()
        if len(q) == 2:
            return q
        
        mid = len(q)//2
        stack = deque()
        for i in range(mid):
            stack.append(q.popleft())
        for i in range(len(q)):
            if q:
                ele = q.popleft()
            if stack:
                q.append(stack.popleft())
            q.append(ele)
        
        return q