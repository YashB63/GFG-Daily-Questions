class Solution:
    def maxSum(self, arr):
        n = len(arr)
        ans = float('-inf')  

        for i in range(1, n):
            ans = max(arr[i] + arr[i - 1], ans)

        return ans