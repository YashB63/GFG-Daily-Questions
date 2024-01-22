class Solution:
    def minimumStep (self, n):
        
        c = 0
        while(n>1):
            if(n%3==0):
                n /= 3
            else:
                n -= 1
            c = c + 1
        return c