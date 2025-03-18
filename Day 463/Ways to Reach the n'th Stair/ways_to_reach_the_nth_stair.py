class Solution:
    def countWays(self, n):
        def f(n):
            if n<0:
                return 0
            if n==0:
                return 1
            if n in dp:
                return dp[n]
            dp[n]=f(n-1)+f(n-2)
            return dp[n]
        dp={}
        return f(n)