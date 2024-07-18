class Solution:

    def findSubArrays(self,arr,n):
        
        ans = 0
        sm = 0
        d = {0:1}
        
        for a in arr:
            sm += a
            if sm in d:
                ans += d[sm]
                d[sm] += 1
            
            else:
                d[sm] = 1
        
        return ans