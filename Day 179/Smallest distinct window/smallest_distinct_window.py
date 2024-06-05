from collections import defaultdict

class Solution:
    def findSubString(self, strr):
        
        n = len(strr)
        l = 0
        r = 0
        
        mapp = defaultdict(lambda: 0)
        
        dist_count = len(set(strr))
        result = n
        while r < n:
            mapp[strr[r]]+=1
            
            if (len(mapp) == dist_count):
                
                while (mapp[strr[l]] > 1):
                    mapp[strr[l]] -= 1
                    l += 1
                result = min(result,r-l+1)
                del mapp[strr[l]]
                l += 1
            r += 1
        return result