from collections import deque

class Solution:
	def xShape(self, grid):
        n=len(grid)
        m=len(grid[0])
        
        def bfs(grid,s,e,visited):
            q=deque()
            q.append((s,e))
            visited[s][e]=True
            d=[(1,0),(0,1),(-1,0),(0,-1)]

            while q:
                c_x,c_y=q.popleft()
                for dx,dy in d:
                    n_x,n_y=c_x+dx,c_y+dy
                    if 0 <= n_x < n and 0 <= n_y < m and not visited[n_x][n_y]:
                        if grid[n_x][n_y]=='X':
                            q.append((n_x,n_y))
                            visited[n_x][n_y]=True
            
        p=0    
        visited=[[False]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if visited[i][j]==False and grid[i][j] == 'X':
                    p+=1
                    bfs(grid,i,j,visited)

        return p