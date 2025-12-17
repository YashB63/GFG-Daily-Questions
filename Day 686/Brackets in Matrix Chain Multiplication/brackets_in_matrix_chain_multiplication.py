class Solution:
    def matrixChainOrder(self, arr):
        n = len(arr)
        dp = [[("", 0) for i in range(n)] for i in range(n)]

        for i in range(n):
            temp = ""

            temp += chr(ord('A') + i)

            dp[i][i] = (temp, 0)

        for length in range(2, n):
            for i in range(n - length):
                j = i + length - 1
                cost = float("inf")
                str = ""

                for k in range(i + 1, j + 1):
                    currCost = (dp[i][k - 1][1] + dp[k][j][1] +
                                arr[i] * arr[k] * arr[j + 1])

                    if currCost < cost:
                        cost = currCost
                        str = "(" + dp[i][k - 1][0] + dp[k][j][0] + ")"

                dp[i][j] = (str, cost)

        return dp[0][n - 2][0]