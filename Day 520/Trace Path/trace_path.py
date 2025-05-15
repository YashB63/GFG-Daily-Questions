class Solution:
    def isPossible(self, n, m, s):
        maxl, maxr, maxu, maxd, c1, c2 = 0, 0, 0, 0, 0, 0
        
        for i in range(len(s)):
            if s[i] == 'L':
                c1 -= 1
            elif s[i] == 'R':
                c1 += 1
            elif s[i] == 'U':
                c2 += 1
            else:
                c2 -= 1
            
            if c1 >= 0:
                maxr = max(c1, maxr)
            else:
                maxl = min(c1, maxl)
            if c2 >= 0:
                maxu = max(c2, maxu)
            else:
                maxd = min(c2, maxd)
        
        if maxr + 1 - maxl <= m and maxu + 1 - maxd <= n:
            return 1
        return 0