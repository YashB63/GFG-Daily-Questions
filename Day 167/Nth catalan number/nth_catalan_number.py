class Solution:
    def findCatalan(self, n : int) -> int:
        
        m = 1000000000 + 7
        c = [0] * (n + 1)
        c[0] = c[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                c[i] += (c[j]  * c[i - j - 1]) % m
        return c[n] % m
