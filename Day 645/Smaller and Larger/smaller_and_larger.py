from bisect import bisect_left, bisect_right

class Solution:
    def getMoreAndLess(self, arr, x):
        l = bisect_left(arr, x)
        r = bisect_right(arr, x)
        return [r, len(arr) - l]