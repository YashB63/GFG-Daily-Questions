import sys
from typing import List
sys.setrecursionlimit(10**8)
from collections import deque
import itertools

class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        
        row= len(grid)
        col = len(grid[0])
        result = set()
        que = deque()
        dr = [ 0, 1 , 0, -1 ]
        dc = [ 1, 0 , -1, 0 ]
        for i,j in itertools.product(range(row),range(col)):
            if grid[i][j] == 1:
                island = []
                que.append((i,j))
                grid[i][j] = 0  
                
                while que:
                    curr, curc = que.popleft()
                    
                    island.append((curr-i,curc-j))
                    
                    for k in range(4):
                        new_i = curr +  dr[k]
                        new_j = curc +  dc[k]
                        if 0<= new_i < row and 0<= new_j < col and grid[new_i][new_j] == 1:
                            grid[new_i][new_j] = 0
                            
                            que.append((new_i,new_j))
                        
                        
                result.add(tuple(island))
                
        return len(result)