class Solution:
	def nthPoint(self,n):
     
        mod = 10**9 + 7
        
        if n == 0:
            return 0
            
        elif n==1:
            return 1
            
        x = [0] * (n+1)
        x[0] = 1
        x[1] = 1
        
        for i in range(2, n+1):
            x[i] = (x[i-1] + x[i-2]) % mod
            
        return x[n]