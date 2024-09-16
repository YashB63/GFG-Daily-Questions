class Solution:
    def fib (self,N):
        a=0
        b=1
        if N==0 or N==1:
            return N
        for i in range(N-1):
            c=a+b
            a=b
            b=c
        return c%10