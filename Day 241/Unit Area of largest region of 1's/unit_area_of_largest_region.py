class Solution:

	def findMaxArea(self, grid):
        def dfs(i,j):
            if i<0 or i>=N or j<0 or j>=M or grid[i][j]==0:
                return 0
            row =[-1,0,1]
            col =[-1,0,1]
            grid[i][j] = 0
            count = 1
            for r in row:
                for c in col:
                    count += dfs(i+r,j+c)
            return count         
        area = 0
        N , M = len(grid),len(grid[0])
        
        for i in range(N):
            for j in range(M):
                if grid[i][j]==1:
                    area = max(area,dfs(i,j))
        return area