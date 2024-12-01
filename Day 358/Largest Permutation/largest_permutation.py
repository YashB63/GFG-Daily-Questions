class Solution:
    def KswapPermutation(self,arr,k):
        i=0
        _max=len(arr)
        d={x:i for i,x in enumerate(arr)}
        while k and i<len(arr):
            j=d[_max]
            if i==j:
                pass
            else:
                k-=1
                arr[i],arr[j]=arr[j],arr[i]
                d[arr[i]],d[arr[j]]=d[arr[j]],d[arr[i]]
            i+=1
            _max-=1
            
        return arr