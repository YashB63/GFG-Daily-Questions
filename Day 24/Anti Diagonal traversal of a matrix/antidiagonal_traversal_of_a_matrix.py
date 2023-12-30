class Solution:
    def antiDiagonalPattern(self,matrix):
       
        x = len(matrix)
        res = []
        if x == 1:
            return [matrix[0][0]]
            
        for i in range(x):
            for j in range(0, i+1):
                res.append(matrix[j][i-j])
        
        for i in range(1, x):
            k = i
            for j in range(x-1, i-1, -1):
                res.append(matrix[k][j])
                k += 1
        
        return res