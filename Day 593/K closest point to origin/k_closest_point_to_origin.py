class Solution:
    def kClosest(self,arr,k):
        d=defaultdict(list)
        
        for e in arr:
            dst=sqrt(e[0]**2+e[1]**2)
            d[dst].append([e[0],e[1]])
            d[dst].sort()
        
        srtdd=sorted(d)
        ans=[]
        for v in srtdd:
            for e in d[v]:
                ans.append(e)
        return ans[:k]