class Solution:
    def sumTriangles(self, mat):
        upper = 0
        lower = 0
        n = len(mat)
        for i in range(n):
            for j in range(n):
                if (i == j):
                    upper += mat[i][j]
                    lower += mat[i][j]

                elif (j > i):
                    upper += mat[i][j]

                elif (j < i):
                    lower += mat[i][j]

        return [upper, lower]