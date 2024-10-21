class Solution:
    def interchange(self,matrix,r,c):
        for i in range(r):
            for j in range(c//2):
                if j==0:
                    matrix[i][0], matrix[i][-1] = matrix[i][-1], matrix[i][0]
            
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=" ")
            print("")