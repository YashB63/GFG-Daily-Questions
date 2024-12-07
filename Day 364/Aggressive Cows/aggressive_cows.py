class Solution:

    def aggressiveCows(self, stalls, k):
        stalls.sort()
        l = 0
        r = stalls[-1]-stalls[0]
        ans = -1
        
        def isValidDist(m,c) -> bool:
            pos = stalls[0]
            for p in stalls:
                if p-pos >= m:
                    c-=1
                    pos = p
                    if c == 1:
                        return True
            return False
        
        while l <= r:
            m = l + (r - l)//2
            if isValidDist(m,k):
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans