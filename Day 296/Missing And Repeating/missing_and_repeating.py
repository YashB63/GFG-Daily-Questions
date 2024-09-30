from collections import Counter

class Solution:
    def findTwoElement( self,arr): 
        d=Counter(arr)
        res=[]
        for i in d:
            if d[i]==2:
                res.append(i)
                break
        i=1
        summ=sum(list(set(arr)))
        t_s=len(arr)*(len(arr)+1)//2
        res.append(t_s-summ)     
        return res