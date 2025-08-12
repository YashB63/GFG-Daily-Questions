class Solution:
    def dyckPaths(self, N):
    	res = 1
    	for i in range(N):
    		res *= (2*N - i)
    		res //= (i + 1)
    
    	ans = res//(N+1)
    	
    	return ans