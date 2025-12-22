class Solution:
     def swapDiagonal(self, mat):
        n = len(mat)
        for i in range(n // 2):
            j = n - 1 - i
            top_row = mat[i]
            top_row[i], top_row[j] = top_row[j], top_row[i]
            bottom_row = mat[j]
            bottom_row[i], bottom_row[j] = bottom_row[j], bottom_row[i]