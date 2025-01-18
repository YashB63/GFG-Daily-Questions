class Solution:
    def maxWater(self, arr):
        max1=0
        l=0
        r=len(arr)-1
        while l<=r:
            t=min(arr[l],arr[r])
            max1=max(max1,(r-l)*t)
            
            if arr[l]<arr[r]:
                l+=1
            else:
                r-=1
        return(max1)
