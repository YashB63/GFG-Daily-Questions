class Solution:
    def computeBeforeMatrix(self, N, M, after):
        for i in range(N-1,-1,-1):
            for  j in range(M-1,-1,-1):
                
                if(i):
                    after[i][j]-=after[i-1][j]
                if(j):
                    after[i][j]-=after[i][j-1]
                
                if(i and j):
                    after[i][j]+=after[i-1][j-1]
            
        return after