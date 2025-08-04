class Solution:
    def countDistinctSubsequences(self, s):
        MOD = 10**9 + 7  
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  
        last_occurrence = {}

        for i in range(1, n + 1):
            dp[i] = 2 * dp[i - 1]
            ch = s[i - 1]
            if ch in last_occurrence:
                dp[i] -= dp[last_occurrence[ch] - 1]
            last_occurrence[ch] = i

        return dp[n]

    def betterString(self, s1, s2):
        a = self.countDistinctSubsequences(s1)
        b = self.countDistinctSubsequences(s2)
        return s2 if b > a else s1