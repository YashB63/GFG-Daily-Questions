class Solution:
    def distinctSubsequences(self, S):
        last = [-1] * 26

        mod = 10**9 + 7

        n = len(S)

        dp = [-2 for i in range(n + 1)]

        dp[0] = 1

        for i in range(1, n + 1):
            dp[i] = 2 * dp[i - 1]
            dp[i] %= mod

            if last[ord(S[i - 1]) - 97] != -1:
                dp[i] = dp[i] - dp[last[ord(S[i - 1]) - 97]]
                dp[i] %= mod
            last[ord(S[i - 1]) - 97] = i - 1

        return dp[n]