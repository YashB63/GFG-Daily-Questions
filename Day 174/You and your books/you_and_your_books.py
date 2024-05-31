class Solution:
    
    def max_Books(self, n, k, arr):
        
        res=0
        cur=0
        for i in range(n):
            if arr[i]<=k:
                cur+=arr[i]
            else:
                cur=0
            res=max(cur,res)
        return res