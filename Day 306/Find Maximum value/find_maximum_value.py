class Solution:
    def maxValue(self, arr):
        n=len(arr)
        ans=[]
        i=0
        j=n-1
        while(i<j):
            res=(abs(i-j)*min(arr[i],arr[j]))
            ans.append(res)
            if(arr[i]<arr[j]):
               i+=1
            else:
               j-=1
        return max(ans)