class Solution:
	def minStepToReachTarget(self, KnightPos, TargetPos, N):
        visited = [[False]*N for _ in range(N)]
        
        start = [N-KnightPos[1],KnightPos[0]-1]
        end = [N-TargetPos[1],TargetPos[0]-1]
        dx = [-2,-2,-1,-1,1,1,2,2]
        dy = [-1,1,-2,2,-2,2,-1,1]
        visited[start[0]][start[1]] = True
        queue = []
        queue.append((start[0],start[1],0))
        
        while len(queue)>0:
            x, y, steps = queue.pop(0)
            
            if [x,y]==end:
                return steps
            for i in range(8):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny,steps+1))