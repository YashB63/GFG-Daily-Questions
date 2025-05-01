class Solution:
    def maxDistance (self, arr, n) : 
        mi=1e9
        ma=-1e9
        mi1=1e9
        ma1=-1e9
        ans=0
        for i,j in enumerate(arr):
            mi=min(mi,j+i)
            ma=max(ma,j+i)
            mi1=min(mi1,j-i)
            ma1=max(ma1,j-i)
           
            
            
        return max(ma-mi,ma1-mi1)