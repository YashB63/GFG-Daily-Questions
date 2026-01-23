import sys

class Solution:
    def multiplyMatrix(self, mat1, mat2, result):
        for i in range(4):
            for j in range(4):
                sum_val = 0
                for k in range(4):
                    sum_val += mat1[i][k] * mat2[k][j]
                if result[i][j] != sum_val:
                    return False
        return True