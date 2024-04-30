class Solution:
    def maxProduct(self, arr, n):
        
        arr.sort()
        return max(arr[0]*arr[1]*arr[-1], arr[-1]*arr[-2]*arr[-3])
