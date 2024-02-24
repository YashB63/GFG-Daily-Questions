class Solution:
    def countSubstring(self, s): 
        
        n = len(s)
        count = 0
        for i in range(n):
            l, u = 0,0
            for j in range(i, n):
                if s[j].islower():
                    l += 1
                else:
                    u += 1
                if l == u:
                    count += 1
        return count