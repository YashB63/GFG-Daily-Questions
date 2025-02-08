class Solution:
	def isWordExist(self, mat, word):
        n, m = len(mat), len(mat[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]  
        
        def dfs(x, y, index):
            if index == len(word):  
                return True
            if x < 0 or x >= n or y < 0 or y >= m or mat[x][y] != word[index]:
                return False
            
            temp = mat[x][y]  
            mat[x][y] = '#' 
            
            for dx, dy in directions:
                if dfs(x + dx, y + dy, index + 1):
                    return True
            
            mat[x][y] = temp 
            return False
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == word[0] and dfs(i, j, 0): 
                    return True
        
        return False