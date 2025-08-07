class Solution:
    def multiply(self, mat1, mat2):
        n = len(mat1)
        result = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result[i][j] += mat1[i][k] * mat2[k][j]

        return result