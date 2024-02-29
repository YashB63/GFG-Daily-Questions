class Solution:
    def orderString(self, s, n):
        
        s.sort()
        r = []
        r.append(s[0])
        r.append(s[len(s) - 1])
        return r