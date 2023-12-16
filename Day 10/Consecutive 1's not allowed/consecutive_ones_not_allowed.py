class Solution:

	def countStrings(self,n):
        MOD = 1000000007
        
        x = [[0,0] for _ in range(n+1)]
        
        x[1][0] = 1
        x[1][1] = 1
        
        for i in range(2, n+1):
            x[i][0] = (x[i-1][0] + x[i-1][1]) % MOD
            x[i][1] = x[i-1][0]
            
        return (x[n][0] + x[n][1]) % MOD