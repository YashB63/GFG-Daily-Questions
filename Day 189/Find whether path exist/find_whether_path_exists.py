class Solution:
    
	def is_Possible(self, grid):
		
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return False
            
            if grid[row][col] == 2:
                return True
            
            temp = grid[row][col]
            grid[row][col] = 0
            
            for di, dj in directions:
                if dfs(di + row, dj + col):
                    return True
            
            grid[row][col] = temp
            return False
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    if dfs(i, j):
                        return True
                    else:
                        return False
        return False