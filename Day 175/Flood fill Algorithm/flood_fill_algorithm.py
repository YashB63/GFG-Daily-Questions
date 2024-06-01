class Solution:
    
    def dfs(self,sr,sc,inc,ans,color):
        n=len(ans)
        m=len(ans[0])
        ans[sr][sc]=color
        directions=[(0,-1),(-1,0),(0,1),(1,0)]
        for dr,dc in directions:
            r=dr+sr
            c=dc+sc
            if(r>=0 and r<n and c>=0 and c<m and ans[r][c]==inc and ans[r][c]!=color):
                self.dfs(r,c,inc,ans,color)
                
	def floodFill(self, image, sr, sc, newColor):
		
        inc=image[sr][sc]
        ans=image
        self.dfs(sr,sc,inc,ans,newColor)
        return ans