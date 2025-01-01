class Solution:
    def setMatrixZeroes(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        
        row_flags = [False] * rows
        col_flags = [False] * cols
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    row_flags[i] = True
                    col_flags[j] = True
        
        for i in range(rows):
            for j in range(cols):
                if row_flags[i] or col_flags[j]:
                    mat[i][j] = 0