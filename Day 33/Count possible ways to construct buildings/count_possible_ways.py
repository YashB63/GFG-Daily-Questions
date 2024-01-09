class Solution:
	def TotalWays(self, N):
		
        x = 1
        y = 1
        mod = int(1e9 + 7)
        
        for _ in range(N):
            y = (x + y)%mod
            x = (y - x)%mod
        return pow(y, 2, mod)