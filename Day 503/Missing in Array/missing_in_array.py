class Solution:
    def missingNum(self, arr):
        n = len(arr) + 1
        tot = n * (n + 1) >> 1
        return tot - sum(arr)
