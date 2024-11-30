class Solution:
    def maxSubArraySum(self,arr):
        n = len(arr)
        lmax = arr[0]
        gmax = arr[0]
        for i in range(1, n):
            if arr[i] > arr[i] + lmax:
                lmax = arr[i]
            else:
                lmax = arr[i]+lmax
            gmax = max(lmax, gmax)
        return gmax