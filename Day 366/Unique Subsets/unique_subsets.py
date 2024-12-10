class Solution:
    
    def AllSubsets(self, arr,n):
        arr.sort()
        ans=set()
        for i in range(1<<n):
            res=[]
            for j in range(n):
                if(i&(1<<j)):
                    res.append(arr[j])
            
            ans.add(tuple(res))
        
        return sorted(ans)