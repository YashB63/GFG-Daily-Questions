class Solution:
	def BoundaryElements(self, matrix):
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i==0 or j==0) or (i==len(matrix)-1 or j==len(matrix[0])-1):
                    res.append(matrix[i][j])
        
        return res