class Solution:
    def findPosition(self, n):
        c=0
        p=0
        l=0
        if n==0:
            return -1
        while n:
            p=p+1
            if n&1==1:
                c=c+1
                l=p
            n=n>>1
        if c==1:
            return l
        else:
            return -1