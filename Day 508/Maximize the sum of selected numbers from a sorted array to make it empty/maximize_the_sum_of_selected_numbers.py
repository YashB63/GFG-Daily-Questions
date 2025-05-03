from collections import Counter

class Solution:
    def maximizeSum (self,arr, n) : 
        d=Counter(arr)
        cnt=0
        l=sorted(d.keys(),reverse=True)
        
        for i in l:
            if d[i]!=0 :
                cnt+=(i*d[i])
                
                
                if i-1 in d:
                    m=min(d[i],d[i-1])
                    
                    d[i-1]-=m
                    
        return cnt