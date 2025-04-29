class Solution:
    def check(self,s1,s2,ind):
            i=0
            n=len(s2)
            j=ind
            while j<len(s1):
                if s2[i]==s1[j]:
                    i+=1
                
                if i>=n:
                    return j-ind+1
                j+=1
            return -1
    def minWindow(self, s1, s2):
        j=0
        mini=999999
        res=""
        while j<len(s1):
            if s1[j]==s2[0]:
                n=self.check(s1,s2,j)
                if n!=-1 and mini>n:
                    mini=n
                    res=s1[j:j+n]
            j+=1
        return res