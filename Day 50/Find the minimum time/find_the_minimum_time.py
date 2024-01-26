class Solution:
    def minTime(self, S1, S2, N):
        
        l = 0
        r = N
        
        res = 10**9
        
        while l <= r:
            
            mid = (l + r) // 2
            temp = max(S1*mid, S2*(N-mid))
            res = min(res, temp)
            if (S1*mid > S2*(N-mid)):
                r = mid - 1
            else:
                l = mid + 1
                
        return res