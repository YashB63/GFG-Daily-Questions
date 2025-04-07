class Solution:
    def maxPartitions(self , s):
        last = {c: i for i, c in enumerate(s)}
        count = end = 0
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                count += 1
        return count