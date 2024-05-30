class Solution:
    def maximumPath(self, N, Matrix):
        
        for i in range(1,N):
            for j in range(N):
                if j>0 and j<N-1:
                    Matrix[i][j]+= max(Matrix[i-1][j] , Matrix[i-1][j-1] , Matrix[i-1][j+1])
                elif j==N-1:
                    Matrix[i][j]+= max(Matrix[i-1][j-1] , Matrix[i-1][j])
                elif j==0:
                    Matrix[i][j]+= max(Matrix[i-1][j] , Matrix[i-1][j+1])
        
        ans=float("-inf")
        for i in range(N):
            ans=max(ans,Matrix[N-1][i])
        return ans