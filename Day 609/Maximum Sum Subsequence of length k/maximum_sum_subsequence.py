def solve(dp, pos, k, arr, n):
    if k < 0:
        return 0

    if dp[pos][k] != -1:
        return dp[pos][k]

    dp[pos][k] = 0

    if k == 1:
        dp[pos][k] = arr[pos][0]
        return dp[pos][k]

    b = 0

    for i in range(pos + 1, n):
        if arr[i][1] < arr[pos][1]:
            x = solve(dp, i, k - 1, arr, n)
            if x > 0:
                dp[pos][k] = max(dp[pos][k], arr[pos][0] + x)
                b = 1

    if b == 0:
        dp[pos][k] = -1 * float('inf')

    return dp[pos][k]


class Solution:
    def max_sum(self, a, k):
        n = len(a)

        dp = [[-1 for i in range(k + 1)] for j in range(n + 1)]

        arr = []
        for i in range(n):
            arr.append([a[i], i])

        arr.sort(reverse=True)

        mx = 0

        for i in range(n):
            x = solve(dp, i, k, arr, n)
            mx = max(mx, x)

        if mx == 0:
            return -1

        return mx