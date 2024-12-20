class Solution:
    def transform(self, A, B): 
        d = {}
        for ch in A:
            d[ch]=d.get(ch,0)+1
            
        for ch in B:
            d[ch] = d.get(ch,0)-1
            
        if any(d.values()):
            return -1
              
        i = len(A) - 1
        j = len(B) - 1
        ans = 0 
        while i>=0 and j>=0:
            if A[i]==B[j]:
                i-=1
                j-=1
            else:
                ans+=1
                i-=1
        return ans