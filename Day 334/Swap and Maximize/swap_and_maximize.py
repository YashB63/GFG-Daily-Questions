class Solution:
    def maxSum(self,arr):
        sum = 0
        arr.sort()
        n = len(arr)
        for i in range(n//2):
            sum -= (2*arr[i])
            sum += (2*arr[n-i-1])
        return sum