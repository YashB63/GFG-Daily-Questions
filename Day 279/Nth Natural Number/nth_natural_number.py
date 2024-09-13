class Solution:
    def findNth(self,n):
        res = 0
        p = 1
        while n>0:
            res += p*(n%9)
            n = n//9
            p = p*10
        return res