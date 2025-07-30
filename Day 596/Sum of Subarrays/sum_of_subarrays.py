class Solution:
    def subarraySum(self, arr):
        n = len(arr)
        result = 0

        for i in range(n):
            result += arr[i] * (i + 1) * (n - i)

        return result