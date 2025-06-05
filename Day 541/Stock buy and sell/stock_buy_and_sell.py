class Solution:
    def stockBuySell(self, arr):
        profit = 0

        for i in range(1, len(arr)):
            if arr[i - 1] < arr[i]:
                profit += arr[i] - arr[i - 1]

        return profit