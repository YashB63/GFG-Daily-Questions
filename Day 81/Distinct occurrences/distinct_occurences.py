class Solution:
    def sequenceCount(self,s, t):
        
        mod = 10**9 + 7
        x, y = len(s), len(t)
        z = [0] * (y + 1)
        z[0] = 1
        for i in range(1, x + 1):
            for j in range(y, 0, -1):
                if s[i - 1] == t[j - 1]:
                    z[j] = (z[j] + z[j - 1]) % mod
                    
        return z[y]