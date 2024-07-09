class Solution:
    def findPath(self, m, n):
      
        def dfs(i,j,move):
            if i==n-1 and j==n-1:
                ans.append(move)
                return
            
            dir="DLRU"
            for idx in range(4):
                nexti = i+di[idx]
                nextj = j+dj[idx]
                if nexti>=0 and nextj>=0 and nexti<n and nextj<n and not vis[nexti][nextj] and m[nexti][nextj]==1:
                    vis[i][j]=1
                    dfs(nexti,nextj,move+dir[idx])
                    vis[i][j]=0
        
        ans=[]
        vis=[[0 for _ in range(n)] for _ in range(n)]
        di = [1,0,0,-1]
        dj = [0,-1,1,0]
        if m[0][0]==1:
            dfs(0,0,"")
        return ans 