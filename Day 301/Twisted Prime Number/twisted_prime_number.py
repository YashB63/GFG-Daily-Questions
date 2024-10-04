import math

class Solution:
    def isPrime(self,n):
        if n == 1:
            return False
        if n == 2:
            return True
        elif n % 2 == 0:
            return False
        for i in range(3,(int(n**0.5))+1,2):
            if n % i == 0:
                return False
        return True
    
    def isTwistedPrime(self,N):
        a = str(N)
        rev = int(a[::-1])
        if self.isPrime(N) and self.isPrime(rev) == True:
            return 1
        return 0