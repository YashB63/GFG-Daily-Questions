class Solution:
    def firstElement (self, n):
        
        a,b=1,0
        while n:
            b,a=a,(a+b)%1000000007
            n-=1
        return b