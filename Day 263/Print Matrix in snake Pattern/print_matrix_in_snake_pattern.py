class Solution:
    def snakePattern(self, matrix): 
        result = []
        n = len(matrix)  

        for i in range(n):
            if i % 2 == 0:
                result.extend(matrix[i])
            else:
                result.extend(matrix[i][::-1])

        return result