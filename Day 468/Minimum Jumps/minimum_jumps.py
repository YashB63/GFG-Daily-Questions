class Solution:
	def minJumps(self, arr):
        from collections import deque
        q= deque([(0,0)])
        for i ,e in enumerate(arr):
            while q and q[0][0] < i:
                q.popleft()
            if not q:
                return -1
            if i+e > q[0][0]:
                q.append((i+e, q[0][1]+1))
        return q[0][1]