from math import sqrt

class Solution:
    def isPrime(self, n : int) -> str:
        
        if n < 2:
            return "No"
        
        for i in range(2,int(sqrt(n))+1):
            
            if n%i==0:
                break
        else:
            return "Yes"
        return "No"