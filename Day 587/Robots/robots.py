class Solution:
    def reduce(self, s1):
        temp=""
        for i in s1:
            if(i!='#'):
                temp+=i
        return temp
    
    def moveRobots (self, s1, s2):
        if(self.reduce(s1)!=self.reduce(s2)):
            return "No"
            
        n = len(s1)
        c = 0

        for i in range(n-1,-1,-1):
            if(s1[i]=='A'):
                c+=1
            if(s2[i]=='A'):
                c-=1
            if(c<0):
                return "No"
        
        c = 0

        for i in range(n):
            if(s1[i]=='B'):
                c+=1
            if(s2[i]=='B'):
                c-=1
            if(c<0):
                return "No"

        return "Yes"