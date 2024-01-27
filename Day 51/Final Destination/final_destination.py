class Solution:
    def canReach(self, a, b, x):
        
        y = abs(a) + abs(b)
        if(x == y):
            return(1)
        elif(x > y and (x - y)%2 == 0):
            return(1)
        else:
            return(0)