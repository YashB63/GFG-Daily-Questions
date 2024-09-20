class Solution:
    def totalCount(self, k, arr):
        total_segments = 0
        for x in arr:
            total_segments += (x // k) + (1 if x % k != 0 else 0)
        return total_segments