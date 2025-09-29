class Solution:
    def revStr (self, s : str) -> str :
        rev_s = ""
        for i in range(len(s)-1,-1,-1):
            rev_s += s[i]
        return rev_s