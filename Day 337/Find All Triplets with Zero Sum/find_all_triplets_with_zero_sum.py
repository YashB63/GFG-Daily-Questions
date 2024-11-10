class Solution:
    def findTriplets(self, arr):
        d={}
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                x=(arr[i]+arr[j])
                if x in d:
                    d[x].append([i,j])
                else:
                    d[x]=[[i,j]]
        
        ans=set()
        
        for i in range(len(arr)):
            if -(arr[i]) in d:
                l=d[-(arr[i])]
                for indices in l:
                    if indices[0]!=i and indices[1]!=i:
                        x=[i]+indices
                        x.sort()
                        x=tuple(x)
                        ans.add(x)
        return list(ans)