class Solution:
    def balanceSums(self, mat):
        n = len(mat)
        res = 0
        maxSum = 0

        for i in range(n):
            row_total = sum(mat[i])
            maxSum = max(row_total, maxSum)

        for j in range(n):
            col_total = sum(mat[i][j] for i in range(n))
            maxSum = max(col_total, maxSum)

        for i in range(n):
            row_total = sum(mat[i])
            res += (maxSum - row_total)

        return res