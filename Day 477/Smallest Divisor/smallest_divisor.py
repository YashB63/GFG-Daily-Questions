class Solution:
    def get_div(self,arr,mid):
        val=0
        for x in arr:
            temp=x//mid
            if((x%mid)!=0):
                temp=temp+1
            val=val+temp
        return val
        
    def smallestDivisor(self, arr, k):
        ans=-1
        l=1
        h=max(arr)
        while(l<=h):
            mid=(l+h)//2
            val=self.get_div(arr,mid)
            
            if(val<=k):
                ans=mid
                h=mid-1
            else:
                l=mid+1
                
        return ans