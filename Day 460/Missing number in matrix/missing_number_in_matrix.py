class Solution:
	def MissingNo(self, matrix):
        N = len(matrix)
        requiredSum = 0
        if 0 in matrix[0]:
            requiredSum = sum(matrix[1])
        else:
            requiredSum = sum(matrix[0])
            
        missingNum = 0
        for row in range(N):
            for col in range(N):
                if matrix[row][col] == 0:
                    matrix[row][col] = requiredSum - sum(matrix[row])
                    missingNum = matrix[row][col]
                    break
        if missingNum <= 0:
            return -1
                
        for row in range(N):
            if sum(matrix[row]) != requiredSum:
                return -1
        for col in range(N):
            sumCol = sum([matrix[row][col] for row in range(N)])
            if sumCol != requiredSum:
                return -1
        
        sumDiagonal1 = sumDiagonal2 =  0
        for i in range(N):
            sumDiagonal1 += matrix[i][i]
            sumDiagonal2 += matrix[i][N-1-i]
        
        if sumDiagonal1 != requiredSum or sumDiagonal2 != requiredSum:
            return -1
        
        return missingNum