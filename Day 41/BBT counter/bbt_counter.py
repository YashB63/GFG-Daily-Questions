class Solution:
    def countBT (self, h):
        
        mod = 10**9 + 7
        x = [0]*(h+1)
        x[1] = 1
        x[2] = 3
        for i in range(3, h+1):
            x[i] = ((x[i-1]*x[i-1])%mod + (x[i-1]*x[i-2]*2)%mod)%mod
        
        return x[h]