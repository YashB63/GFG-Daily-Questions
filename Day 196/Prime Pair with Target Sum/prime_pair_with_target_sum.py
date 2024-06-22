from typing import List

class Solution:
    def getPrimes(self, n : int) -> List[int]:
   
        def prime(n):
            if  n <= 1:
                return False
            for i in range(2,int(n**0.5)+1):
                if n % i == 0:
                    return False 
            return True 
        if n == 4:
            return [2,2]
        if  n % 2 == 1:
            if  prime(n-2) == True :
                return [2,n-2]
            return [-1,-1]
        for i in range(3,(n//2)+1,2):
            if prime(i) == True and prime(n-i) == True :
                return [i,n-i]
        return [-1,-1]