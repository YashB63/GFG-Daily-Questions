class Solution:
    def fibSum (self,N):
        MOD = 1000000007
        if N == 0:
            return 0
        elif N == 1:
            return 1
        
        a, b = 0, 1
        fib_sum = a + b
        
        for i in range(2, N + 1):
            a, b = b, (a + b) % MOD
            fib_sum = (fib_sum + b) % MOD
        
        return fib_sum