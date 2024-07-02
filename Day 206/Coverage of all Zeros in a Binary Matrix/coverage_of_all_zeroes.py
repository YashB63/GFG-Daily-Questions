class Solution:
	def findCoverage(self, matrix):
		
        count=0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    if j + 1 < m and matrix[i][j+1]==1:
                         count=count+1
                    if  i + 1 < n and matrix[i+1][j]==1:
                        count+=1
                    if j - 1 >= 0 and matrix[i][j - 1] == 1:
                        count += 1
                    if i - 1 >= 0 and matrix[i - 1][j] == 1:
                         count += 1
        return count
