class Solution:
	def getCount(self, n):
		
        arr = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
        dp = {}
        def solve(i,j,n):
            if i<0 or i>3 or j<0 or j>2 or arr[i][j] in ("#","*"):
                return 0
            n-=1
            if n == 0:
                return 1
            if (i,j,n) in dp:
                return dp[(i,j,n)]
            
            dp[(i,j,n)] = 0
            for p,q in [[0,1],[1,0],[0,-1],[-1,0]]:
                new_i = i+p
                new_j = j+q
                
                dp[(i,j,n)] += solve(new_i,new_j,n)
            
            dp[(i,j,n)] += solve(i,j,n)
            return dp[(i,j,n)]
        ans = 0
        for i in range(0,4):
            for j in range(3):
                if arr[i][j] not in ("#","*"):
                    ans += solve(i,j,n)
        return ans