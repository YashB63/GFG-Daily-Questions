import bisect

class Solution:
    def lis(self, arr):
        sub = []
        for i in arr:
            idx = bisect.bisect_left(sub, i)
            if idx == len(sub):
                sub.append(i)
            else:
                sub[idx] = i
        return len(sub)