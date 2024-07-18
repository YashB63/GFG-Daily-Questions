class Solution:
        
    def minSwap (self,arr, n, k) : 
        
        cnt = 0
        bad = 0
        for i in range(n):
            if arr[i]<=k:
                cnt+=1
                
        for i in range(0, cnt):
            if arr[i]>k:
                bad+=1
                
        i = 0
        j = cnt
        ans = bad
        
        while j<n:
            if arr[i]>k:
                bad-=1
            if arr[j]>k:
                bad+=1
            ans = min(ans, bad)
            i+=1
            j+=1
            
        return ans