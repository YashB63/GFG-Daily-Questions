import math

class Solution:
    def solve(self, mid, arr):
        ans = 0
        
        for i in arr:
            ans+=math.ceil(i/mid)
            
        return ans
        
    def kokoEat(self,arr,k):
        i, j = 1, max(arr)
        ans = -1
        
        while i<=j:
            mid = i+(j-i)//2
            time = self.solve(mid, arr)
            
            if time <= k:
                ans = mid
                j = mid - 1
            else:
                i = mid + 1
                
        return ans