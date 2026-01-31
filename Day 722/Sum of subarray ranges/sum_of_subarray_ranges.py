class Solution:
    def subarrayRanges(self, arr):
        MAX_VALUE = 10**9
        
        def max_range_sum(arr):
            s = [(MAX_VALUE + 1, -1)]
            arr.append(MAX_VALUE)
            sumi = 0
            for i, a in enumerate(arr):
                while s[-1][0] <= a:
                    b, j = s.pop()
                    sumi += (i - j) * (j - s[-1][1]) * b
                s.append((a, i))
            return sumi
        
        neg_arr = [-a for a in arr]
        return max_range_sum(arr) + max_range_sum(neg_arr)