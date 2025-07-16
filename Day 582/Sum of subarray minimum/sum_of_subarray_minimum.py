class Solution:
    def sumSubMins(self, arr):
        n = len(arr)
        dp = [0] * n
        right = [i for i in range(n)]
        stack = []

        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                right[stack.pop()] = i
            stack.append(i)

        dp[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            r = right[i]
            if r == i:
                dp[i] = (n - i) * arr[i]
            else:
                dp[i] = (r - i) * arr[i] + dp[r]

        return sum(dp)