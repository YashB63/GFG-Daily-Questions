class Solution:
    def overlapInt(self, arr):
        from heapq import heappop, heappush
        arr.sort()
        ends = []
        max_overlap = 0
        for start, end in arr:
            while ends and ends[0] < start:
                heappop(ends)
            heappush(ends, end)
            if (l := len(ends)) > max_overlap:
                max_overlap = l
        return max_overlap