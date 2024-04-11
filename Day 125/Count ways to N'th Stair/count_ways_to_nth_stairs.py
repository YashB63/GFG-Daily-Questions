class Solution:

    def countWays(self, n):

        mod = 1000000007
    
        twoCount=n//2
        return (twoCount+1)%mod