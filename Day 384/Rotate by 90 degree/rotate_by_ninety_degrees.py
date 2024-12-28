class Solution:
    
    def rotateby90(self, mat): 
        n = len(mat)
    
        for i in range(n):
            for j in range(i, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
        for j in range(n):
            for i in range(n // 2):
                mat[i][j], mat[n - i - 1][j] = mat[n - i - 1][j], mat[i][j]
