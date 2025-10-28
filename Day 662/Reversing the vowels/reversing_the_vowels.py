class Solution:
    def modify(self, s: str) -> str:
        vow = ""
        s = list(s)  
        
        for i in range(len(s)):
            if s[i] in 'aeiou':
                vow += s[i]
                s[i] = '.'  
        
        i = len(s) - 1
        j = 0
        while i >= 0:
            if s[i] == '.':
                s[i] = vow[j]
                j += 1
            i -= 1
        
        return ''.join(s)