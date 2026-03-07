class Solution:
    def heapHeight(self, n, arr):
        count = 1
        i = 0
        mul = 1
        while i < n - 1:
            if i + mul * 2 < n - 1:
                count += 1
            mul *= 2
            i += mul
        return count