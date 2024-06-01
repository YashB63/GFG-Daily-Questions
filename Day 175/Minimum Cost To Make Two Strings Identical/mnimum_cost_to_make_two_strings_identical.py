class Solution:
	def findMinCost(self, x, y, costX, costY):
		
        X, Y = len(x), len(y)
        
        dp = [[0] * (Y+1) for _ in range(X+1)]
        
        for i in reversed(range(X)):
            for j in reversed(range(Y)):
                if x[i] == y[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                    
        lcs = dp[0][0]
        
        return costX * (X - lcs) + costY * (Y-lcs)
