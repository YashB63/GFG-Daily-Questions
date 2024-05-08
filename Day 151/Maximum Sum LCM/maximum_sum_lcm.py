class Solution:
    def maxSumLCM (self, n):
        
        res=0
        
        for j in range(1,int(n**0.5)+1):
            if n%j==0:
                res+=j
                if j!=n/j:
                    res+=n/j
                    
        return int(res)