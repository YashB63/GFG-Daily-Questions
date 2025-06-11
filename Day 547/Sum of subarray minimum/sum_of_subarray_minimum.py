class Solution:
    def sumSubarrayMins(self, arr):
        MOD = int(1e9 + 7)
        n = len(arr)
        left = [0] * n
        right = [0] * n

        for i in range(n):
            right[i] = n - 1 - i

        for i in range(n - 1, -1, -1):
            left[i] = i

        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                right[stack[-1]] = i - stack[-1] - 1
                stack.pop()
            stack.append(i)

        stack.clear()

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                left[stack[-1]] = stack[-1] - i - 1
                stack.pop()
            stack.append(i)

        ans = 0

        for i in range(n):
            ans = (ans + arr[i] * (left[i] + 1) * (right[i] + 1)) % MOD

        return ans