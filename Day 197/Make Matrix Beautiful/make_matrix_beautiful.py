class Solution:
    def findMinOpeartion(self, matrix, n):
        
        rs=[0]*n
        cs=[0]*n

        for i in range(n):
            for j in range (n):
                rs[i]+=matrix[i][j]
                cs[i]+=matrix[j][i]
                
        ms=max(max(rs),max(cs))
        res=0
        for i in range(n):
            res+=ms-rs[i]
        return res