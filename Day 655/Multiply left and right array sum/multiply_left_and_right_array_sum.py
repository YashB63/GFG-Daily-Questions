class Solution:
    def multiply(self, arr):
        sum1, sum2 = 0, 0
        n = len(arr)

        for i in range(n // 2):
            sum1 += arr[i]

        for i in range(n // 2, n):
            sum2 += arr[i]

        return sum1 * sum2