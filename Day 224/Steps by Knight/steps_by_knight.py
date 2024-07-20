import collections
class Solution:

	def minStepToReachTarget(self, KnightPos, TargetPos, n):
		
        a, b = KnightPos[0]-1,KnightPos[1]-1
        x, y = TargetPos[0]-1, TargetPos[1]-1
        if (a,b) == (x,y): return 0
        
        q = collections.deque()
        q.append((a, b, 0)) 
        vis = set()
        vis.add((a, b))
        
        while q:
            r, c, steps = q.popleft()
            if r == x and c == y:
                return steps
            
            d = [(-1, -2), (-1, 2), (1, 2), (1, -2), (2, -1), (2, 1), (-2, 1), (-2, -1)]
            for dx, dy in d:
                row, col = r + dx, c + dy
                if 0 <= row < n and 0 <= col < n and (row, col) not in vis:
                    vis.add((row, col))
                    q.append((row, col, steps + 1))
        
        return -1