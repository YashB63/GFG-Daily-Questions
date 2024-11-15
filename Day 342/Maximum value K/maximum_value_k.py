class Solution:
    def findMaximumNum(self, arr):
        arr.sort()
        n = len(arr)
        res = -1

        for i in range(n):
            k = n - i
            if arr[i] >= k:
                res = max(res, k)
        
        return res