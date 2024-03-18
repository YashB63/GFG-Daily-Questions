class Solution:
    def matrixDiagonally(self,mat):
        
        n, d = len(mat), dict()
        
        for i in range(n):
            for j in range(n):
                d[i+j] = d.get(i+j, []) + [mat[i][j]]
        
        res = []
        for key, val in d.items():
            res += val[::-1] if key%2==0 else val
        
        return res