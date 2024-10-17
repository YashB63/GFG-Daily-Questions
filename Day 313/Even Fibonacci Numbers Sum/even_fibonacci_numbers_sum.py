class Solution:
    def evenFibSum (self, N):
        MOD = (10**9) + 7
        a,b,sum1 = 0,1,0
        while b <= N:
            if b % 2 == 0:
                sum1 += b
            a,b = b,a+b
        return sum1