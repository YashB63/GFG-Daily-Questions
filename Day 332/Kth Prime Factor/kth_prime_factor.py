import math

class Solution:
    def kthPrime(self, n, k):
        while n%2==0:
            n//=2
            k-=1
            if k==0:
                return 2
        
        for i in range(3,math.ceil(n**0.5)+1,2):
            while n%i == 0:
                n//=i
                k-=1
                if k==0:
                    return i
       
        if(k==1 and n>2):
            return n

        return -1