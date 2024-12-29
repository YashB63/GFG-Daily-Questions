from collections import deque

class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        source=(0,0)
        destination=(X,Y)
        if source[0]==destination[0] and source[1]==destination[1]:
            return 0
        if A[0][0]==0:
            return -1
        q=deque()
        dist=[[float('inf') for _ in range(M)] for _ in range(N)]
        q.append((0,(source[0],source[1])))
        directions=[(-1,0),(0,-1),(0,1),(1,0)]
        
        while q:
            dis,(r,c)=q.popleft()
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if 0<=nr<N and 0<=nc<M and A[nr][nc]==1 and dis+1<dist[nr][nc]:
                    dist[nr][nc]=1+dis
                    if nr==destination[0] and nc==destination[1]:
                        return 1+dis
                    q.append((1+dis,(nr,nc)))
        return -1