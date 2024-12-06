class Solution:
    
    def areAnagrams(self, s1, s2):
        s1=list(s1)
        s2=list(s2)
        s1.sort()
        s2.sort()
        if len(s1)!=len(s2):
            return False
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                return False
        return True