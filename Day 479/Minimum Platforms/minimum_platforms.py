class Solution:    
    def minimumPlatform(self,arr,dep):
        n = len(arr)
        arr.sort()
        dep.sort()
        curr=res=i=1
        j=0
        while i<n and j<n:
            if arr[i]<=dep[j]:
                curr+=1
                i+=1
            else:
                curr-=1
                j+=1
            res=max(res,curr)
        return res