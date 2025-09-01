class Solution:
    def generatePal(self, s, isPalin):
        n = len(s)

        for i in range(n):
            isPalin[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j] and (length == 2 or isPalin[i + 1][j - 1]):
                    isPalin[i][j] = True

    def palPartition(self, s):
        n = len(s)

        isPalin = [[False] * n for _ in range(n)]

        self.generatePal(s, isPalin)

        dp = [n] * n

        dp[0] = 0

        for i in range(1, n):
            if isPalin[0][i]:
                dp[i] = 0
            else:
                for j in range(i, 0, -1):
                    if isPalin[j][i]:
                        dp[i] = min(dp[i], 1 + dp[j - 1])

        return dp[n - 1]