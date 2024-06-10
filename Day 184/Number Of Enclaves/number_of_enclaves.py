from typing import List
from collections import deque

class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        
        n,m = len(grid), len(grid[0])
        vis = [[0]*m for _ in range(n)]
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
        c = 0
        
        
        for i in range(n):
            for j in range(m):
                if (i == 0 or j == 0 or i == n-1 or j == m-1):
                    if grid[i][j] == 1:
                        self.bfs(i,j,grid,vis,n,m)
        
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and vis[i][j] == 0:
                    c += 1
        
        return c
        
    def bfs(self, r,c,grid,vis,n,m):
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
        
        q = deque()
        q.append([r,c])
        
        vis[r][c] = 1
        while q:
            row,col = q.popleft()
            for i in range(4):
                nr = dr[i] + row
                nc = dc[i] + col
                if (nr >= 0 and nr < n) and (nc >= 0 and nc < m) and grid[nr][nc] == 1 and vis[nr][nc] == 0:
                    q.append([nr,nc])
                    vis[nr][nc] = 1