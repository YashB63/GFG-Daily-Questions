class Solution:
    def countWays(self,n,k):

        mod = 1000000007
        
        if n == 0:
            return 0
            
        if n==1:
            return k
            
        same, diff = k, k * (k-1)
        
        for i in range(3, n+1):
            same, diff = diff, (same + diff) * (k-1) % mod
            
        return (same + diff) % mod