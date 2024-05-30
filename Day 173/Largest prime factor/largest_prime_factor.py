class Solution:
    def largestPrimeFactor (self, N):
        
        f = -1
        while N % 2 == 0:
            f = 2
            N >>= 1
        while N % 3 == 0:
            f = 3
            N //= 3
        i = 5
        while i * i <= N:
            while N % i == 0:
                f = i
                N //= i
            while N % (i + 2) == 0:
                f = i + 2
                N //= i + 2
            i += 1
        if N > 4:
            f = N
        return f