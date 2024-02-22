class Solution:

    def fun(self, s,k,n,c):
        
        co = s.count(c)
        
        l = len(s)
        
        q = n // l
        r = n % l
        
        t1 = q * co
        t2 = s[: r].count(c)
        
        return t1 + t2