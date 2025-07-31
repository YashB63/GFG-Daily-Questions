class Solution:
    def max_non_overlapping(self,ranges):
        n = len(ranges)
        if n <= 1:
            return n
        
        ranges.sort(key=lambda ranges: ranges[0])
        
        end = ranges[0][1]
        max = 1
        
        for i in range(n):
            if ranges[i][0] < end:
                end = min(end,ranges[i][1])
            else:
                max += 1
                end = ranges[i][1]
        return max