class Solution:
    def initials(self,N,M):
        self.n=N
        self.m=M
    def find(self,nr,nc):
        if(nr<0 or nc<0 or nr>self.n-1 or nc>self.m-1):
            return False
        return True
    def closedIslands(self, matrix, N, M):
        self.initials(N,M)
        q=[]
        count=0
        r=[-1,0,1,0]
        c=[0,-1,0,1]
        for i in range(N):
            for j in range(M):
                if((i==0 or j==0 or i==N-1 or j==M-1) and matrix[i][j]==1):
                    matrix[i][j]=0
                    q.append([i,j])
        while len(q)!=0:
             a,b=q.pop(0)
             for i in range(4):
                 nr=r[i]+a
                 nc=c[i]+b
                 if(self.find(nr,nc) and matrix[nr][nc]==1):
                     matrix[nr][nc]=0
                     q.append([nr,nc])
        for i in range(N):
               for j in range(M):
                   if(matrix[i][j]==1):
                       count+=1
                       q.append([i,j])
                       while len(q)!=0:
                           a,b=q.pop(0)
                           for ii in range(4):
                                nr=r[ii]+a
                                nc=c[ii]+b
                                if(self.find(nr,nc) and matrix[nr][nc]==1):
                                   matrix[nr][nc]=0
                                   q.append([nr,nc])
        return count