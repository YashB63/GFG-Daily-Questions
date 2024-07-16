class Solution:
    #Function to count number of ways to reach the nth stair.
    def countWays(self,n):
        def f(n, dp):
            if n == 0:
                return 1
            if n == 1:
                return 1
            if n == 2:
                return 2
            if dp[n] != -1:
                return dp[n]
            one_step = f(n - 1, dp)
            two_step = f(n - 2, dp)
            dp[n] = one_step + two_step
            return (dp[n]% 1000000007)

        dp = [-1] * (n + 1)
        return f(n, dp)