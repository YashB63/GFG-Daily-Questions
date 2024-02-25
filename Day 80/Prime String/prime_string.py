import math

def isPrime(n):
    
    if n== 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n%i == 0:
            return False
    return True

class Solution:
    def isPrimeString(self, s):
       
        count = 0
        for i in s:
            count += ord(i)
        if isPrime(count):
            return True
        else:
            return False