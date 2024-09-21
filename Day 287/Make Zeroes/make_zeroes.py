class Solution:
	def MakeZeros(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        temp={}  
        
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 0:
                    s = 0
                    if -1<col + 1 < m:  # Right
                        s += matrix[row][col + 1]
                        temp[(row, col+1)]=0
                        
                    if -1<row + 1 < n:  # Down
                        s += matrix[row + 1][col]
                        temp[(row+1, col)]=0
                        
                    if n>row - 1 >= 0:  # Up
                        s += matrix[row - 1][col]
                        temp[(row-1, col)]=0
                    if m>col - 1 >= 0:  # Left
                        s += matrix[row][col - 1]
                        
                        temp[(row, col-1)]=0
                        
                    temp[(row, col)] = s 
        
        for x,y in temp:
            matrix[x][y]=temp[(x,y)]