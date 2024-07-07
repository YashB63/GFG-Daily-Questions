from collections import deque
import sys
sys.setrecursionlimit(10**8)
class Solution:
    def numIslands(self,grid):
        
        n = len(grid)
        m = len(grid[0])
        vis = [[False]*m for _ in range(n)]
        count = 0

        def bfs(grid, node, n, m):
            vis[node[0]][node[1]] = True
            q = deque([node])
            while q:
                el = q.pop()
                row, col = el[0], el[1]
                for i in range(-1,2): 
                    for j in range(-1,2):
                        curr_row = row+i
                        curr_col = col+j
                        if (0<=curr_row<n) and (0<=curr_col<m) and grid[curr_row][curr_col]==1 and vis[curr_row][curr_col] == False:
                            vis[curr_row][curr_col] = True
                            q.appendleft([curr_row, curr_col])
                

        for i in range(n):
            for j in range(m):
                if (vis[i][j] == False and grid[i][j]==1):
                    count += 1
                    bfs(grid, [i,j], n, m)
        return count