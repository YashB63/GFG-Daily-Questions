class Solution:
    def findMaxSum(self,n,m,mat):
        
        if n < 3:
            return -1
            
        res = 0
        curr = 0
        
        for i in range(n - 2):
            for j in range(m - 2):
                
                curr = ( mat[i][j] + mat[i][j + 1] + mat[i][j + 2] + 
                        mat[i + 1][j + 1] + 
                        mat[i + 2][j] + mat[i + 2][j + 1] + mat[i + 2][j + 2])
                        
                res = max(curr, res)
                
        return res