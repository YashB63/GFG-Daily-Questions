class Solution:
    def maximiseSubset(self, arr, n, k):
        
        res = k
        x = 0
        y = 0
        
        while (x<n):
            while ((arr[x] - arr[y]) - (x-y) > k):
                y += 1
            res = max(res, x - y + k + 1)
            x += 1
        return (res)