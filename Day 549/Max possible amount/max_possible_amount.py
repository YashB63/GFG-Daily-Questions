class Solution:
    def maxAmount(self, A, N):
        dp = [[[0, 0] for i in range(N)] for j in range(N)]
        arr = A[:]

        dp[0][0] = [A[0], 0]
        for i in range(1, N):
            arr[i] += arr[i - 1]
            dp[i][i] = [A[i], 0]

        col = 0

        while col < N:
            col += 1

            for row in range(N - col):
                L, R = row, row + col

                m1 = A[L] + dp[L + 1][R][1]
                m2 = A[R] + dp[L][R - 1][1]
                x = max(m1, m2)

                dp[L][R] = [x, arr[R] - arr[L] + A[L] - x]

        return dp[0][-1][0]