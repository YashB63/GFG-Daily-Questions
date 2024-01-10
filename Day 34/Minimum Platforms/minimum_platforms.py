class Solution:    
    
    def minimumPlatform(self,n,arr,dep):
       
        arr.sort()
        dep.sort()
        x = 1
        res = 1
        i = 1
        j = 0
        
        while i < n and j < n:
            if arr[i] <= dep[j]:
                x += 1
                i += 1
                res = max(res, x)
                
            else:
                x -= 1
                j += 1
                
        return res