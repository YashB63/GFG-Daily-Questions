class Solution:
    def LCP(self,arr,n):
        arr.sort()
        
        fst=arr[0]
        lcp=len(fst)
        
        for e in arr:
            i=0
            
            while fst[i]==e[i]:
                i+=1
                
                if i>=lcp or i>=len(e):
                    break
            
            if i<lcp:
                lcp=i
                
        if lcp==0:
            return -1
        return fst[:lcp]