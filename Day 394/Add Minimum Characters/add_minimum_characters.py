class Solution:
    def addMinChar (self, s):
        i=0
        
        l=len(s)
        j=l-1
        c=0
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            
            else:
                i=0
                c+=1
                l-=1
                j=l-1
                
        return c