from collections import deque

class Solution:
    def shortestXYDist(self, grid, N, M):
        dq=deque()
        visited=[[False for j in range(M)] for i in range(N)]
        for i in range(N):
            for j in range(M):
                if grid[i][j]=='X':
                    dq.append([i,j])
        
        level=0
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        
        while dq:
            size=len(dq)
            for _ in range(size):
                i,j=dq.popleft()
                if not visited[i][j]:
                    visited[i][j]=True
                    if grid[i][j]=='Y':
                        return level
                    for k in range(4):
                        x=dx[k]+i
                        y=dy[k]+j
                        if 0<=x<N and 0<=y<M and grid[x][y]!='X' and not visited[x][y]:
                            dq.append([x,y])
            level+=1
        return -1