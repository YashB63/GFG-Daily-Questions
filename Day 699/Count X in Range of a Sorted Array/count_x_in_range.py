from bisect import bisect_left, bisect_right

class Solution:
    def countXInRange(self, arr, queries):
        def count(l, r, x):
            left = bisect_left(arr, x, l, r + 1)
            right = bisect_right(arr, x, l, r + 1)
            return right - left
        
        return [count(*query) for query in queries]