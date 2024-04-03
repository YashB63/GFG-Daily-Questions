class Solution:
	def matSearch(self,mat, N, M, X):
		
        r, c = 0, M-1
        def inBounds(r,c):
            return r >= 0 and r < N and c >= 0 and c < M
            
        while inBounds(r,c):
            if mat[r][c] == X: return 1
            
            elif mat[r][c] < X:
                r += 1
            elif mat[r][c] > X:
                c -= 1
                
        return 0