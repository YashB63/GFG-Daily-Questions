class Solution:
    def permutationCoeff(self, n, k):
        p = 1
        mod = int(1e9 + 7)
        
        for i in range(k):
            p = (p * (n - i)) % mod
        
        return (p + mod) % mod