class Solution:
    def convertToEven(self, s):
        
        c=0
        for i in range(len(s)):
            if s[i]=='O' and i==0:
                c=c+1
            elif(i>0 and s[i]=='O' and s[i-1]=="E"):
                c=c+1
        return c