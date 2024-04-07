class Solution:
    def transpose(self, matrix, n):
        
        for i in range(n):
            for j in range(i+1,n):
                temp = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = temp
        return matrix