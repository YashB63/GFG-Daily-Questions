class Solution:
    def removeUtil (self, s):
        if len(s) <= 1:
            return s
        
        new_str = []
        i = 0
        
        while i < len(s):
            if i + 1 < len(s) and s[i] == s[i + 1]:
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    i += 1
            else:
                new_str.append(s[i])
            i += 1
        
        new_s = ''.join(new_str)
        if new_s == s:
            return new_s
        return self.removeUtil(new_s)  