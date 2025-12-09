class Solution:
    def removeChars(ob, str1, str2):
        res = ""
        
        for i in str1:
            if(i in str2):
                continue
            else:
                res += i
        
        return res