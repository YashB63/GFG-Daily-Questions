class Solution:
    def searchRowMatrix(self, mat, x): 
    	a = len(mat)
        for i in range(a):
            for j in range(len(mat[i])):
                if x==mat[i][j]:
                    return True
        return False
