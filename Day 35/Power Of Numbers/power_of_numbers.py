class Solution:
    
    def power(self,N,R):
        
        mod = 1000000007
        res = pow(N, R, mod)
        return int(res)
