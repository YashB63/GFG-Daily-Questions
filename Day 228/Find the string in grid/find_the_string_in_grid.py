class Solution:
	def searchWord(self, grid, word):
		
        ans=[]
        dr=[-1,0,1,0,-1,1,1,-1]
        dc=[0,1,0,-1,1,1,-1,-1]
        m=len(grid[0])
        n=len(grid)
        l=len(word)
        
        def valid(i,j):
            if 0<=i<n and 0<=j<m: 
                return True
                
        def dfs(r,c,k,ind):
            if ind==l:
                return True
            if valid(r,c) and grid[r][c]==word[ind]:
                return dfs(r+dr[k],c+dc[k],k,ind+1)
            return False
           
          
        for i in range(n):
            for j in range(m):
                if grid[i][j]==word[0]:
                    p=False
                    if l==1:
                        ans.append((i,j))
                        continue
                    for k in range(8):
                        if dfs(i,j,k,0):
                            ans.append((i,j))
                            break
        return ans