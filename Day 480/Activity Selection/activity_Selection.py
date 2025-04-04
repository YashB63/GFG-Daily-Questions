class Solution:
    def activitySelection(self, start, finish):
        act = zip(start, finish)
        act = sorted(act, key=lambda x: x[1])
        
        res = 1
        last = act[0]
        for s,f in act[1:]:
            if last[1] >= s:
                continue
            res += 1
            last = (s,f)
        return res