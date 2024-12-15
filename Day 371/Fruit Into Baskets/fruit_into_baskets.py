class Solution:
    def totalFruits(self,arr):
        n = len(arr)
        l = r = maxi = 0
        d = {}
        while r < n:
            if arr[r] in d:
                d[arr[r]] += 1
            else:
                d[arr[r]] = 1
            if len(d) > 2:
                d[arr[l]] -= 1
                if d[arr[l]] == 0:
                    del d[arr[l]]
                l += 1
            else:
                maxi = max(maxi, r - l + 1)
            r += 1
        return maxi
