class Solution:
    def sum(self, freq, i, j):
        s = 0
        for k in range(i, j + 1):
            s += freq[k]
        return s

    def minCost(self, keys, freq):
        n = len(keys)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = freq[i]

        for l in range(2, n + 1):
            for i in range(0, n - l + 1):
                j = i + l - 1
                dp[i][j] = float('inf')

                fsum = self.sum(freq, i, j)

                for r in range(i, j + 1):
                    c = (dp[i][r - 1] if r > i else 0) + (dp[r + 1][j] if r < j
                                                          else 0) + fsum
                    if c < dp[i][j]:
                        dp[i][j] = c

        return dp[0][n - 1]