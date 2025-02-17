from collections import deque
from typing import List

class Solution:
    def chefAndWells(self, n : int, m : int, c : List[List[str]]) -> List[List[int]]:
        coordinates = [[-1,0], [0,-1], [1,0], [0,1]]
        result = [[0 for i in range(m)] for i in range(n)]
        queue = deque()
        
        for i in range(n):
            for j in range(m):
                if c[i][j] == 'W':
                    queue.append([i,j])
        
        level = 1
        while queue:
            size = len(queue)
            while size:
                x, y = queue.popleft()

                for dx, dy in coordinates:
                    i = x + dx
                    j = y + dy

                    if 0 <= i < n and 0 <= j < m and (c[i][j] == 'H' or c[i][j] == '.'):
                        if c[i][j] == 'H':
                            result[i][j] = 2*level
                        
                        c[i][j] = 'X'
                        queue.append([i,j])
                
                size -= 1
            level += 1
        
        for i in range(n):
            for j in range(m):
                if c[i][j] == 'H':
                    result[i][j] = -1
        
        return result