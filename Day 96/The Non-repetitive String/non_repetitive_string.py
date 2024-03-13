class Solution:
    def nonRepetitive(self, s):
        
        s1=set()
        aa=True
        
        for i in range(len(s)):
            
            if s[i] not in  s1:
                s1.add(s[i])
            else:
                if s[i]==s[i-1]:
                    pass 
                else:
                    aa=False
                    return 0
        if aa ==True :
            return 1