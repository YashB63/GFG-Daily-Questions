class Solution:

    def aggressiveCows(self, stalls, k):
        stalls.sort()
        n = len(stalls)
        
        def canPlace(dis):
            cnt = 1
            last = stalls[0]
            for i in range(1, n):
                if stalls[i] - last >= dis:
                    cnt += 1
                    last = stalls[i]
                    if cnt == k:
                        return True
                        
        l, r = 1, stalls[-1]-stalls[0]
        ans = 0
        while l<=r:
            mid = l + (r-l)//2
            if canPlace(mid):
                ans = mid
                l = mid+1
            else:
                r = mid-1
                
        return ans