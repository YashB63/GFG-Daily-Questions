class Solution:
    def stringSort (self,s):
        
        str1 = ""
        str2 = ""
        
        for i in s:
            if ord(i)>=65 and ord(i)<=91:
                str1 += i
            else:
                str2 += i
                
        str1 = sorted(str1)
        str2 = sorted(str2)
        s1 = len(str1)
        s2 = len(str2)
        res = []
        for i in range(min(s1,s2)):
            res+=str1[i]
            res += str2[i]
            
        if s1>s2:
            res += str1[s2:]
        elif s2>s1:
            res += str2[s1:]
        return ''.join(res)