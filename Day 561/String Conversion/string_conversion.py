class Solution:
    def stringConversion(self, X, Y):
        n = len(X)
        m = len(Y)

        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        
        dp[0][0] = 1

        for i in range(n):
            for j in range(m + 1):
                if dp[i][j]:
                    if j < m and X[i].upper() == Y[j]:
                        dp[i + 1][j + 1] = 1
                    if not X[i].isupper():
                        dp[i + 1][j] = 1

        return dp[n][m]
