class Solution:
    def isDeficient (self, x):
        
        s = 0
        for i in range(1, x+1):
            if(x%i == 0):
                s += i
            
        if(s < 2*x):
            return "YES"
        else:
            return "NO"