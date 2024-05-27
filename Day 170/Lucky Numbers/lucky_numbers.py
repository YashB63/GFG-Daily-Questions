class Solution:
    def isLucky(self, n): 
        
        counter = 2
        while n >= counter:
            if n % counter == 0:
                return 0
            n -= n // counter
            counter += 1
        return 1