class Solution:
    def reverseEqn(self, s):
        
        res, sub = '', ''
        for i in range(len(s) - 1, -1, -1):
            if s[i].isdigit():
                sub += s[i]
            else:
                sub = sub[::-1]
                res += sub
                res += s[i]
                sub = ''
        
        sub = sub[::-1]
        res += sub
        return res