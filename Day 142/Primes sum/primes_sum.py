import math
class Solution:
    def isSumOfTwo (self, N):
        
        if N>3:
            if N%2==0:
                return("Yes")
            else:
                if self.is_Prime(N-2):
                    return("Yes")
                else:
                    return("No")
        else:
            return "No"
    
    def is_Prime(self,n):
        no_of_factors = 0
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                no_of_factors +=1
        
        if no_of_factors==0:
            return True
        else:
            return False