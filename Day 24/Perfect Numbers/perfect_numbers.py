class Solution:
    def isPerfectNumber(self, N):
        
        if(N <= 1):
            return 0
        
        s = 1
        temp = N
        
        for i in range(2, int(N**0.5) + 1):
            if (N%i == 0):
                s += i
                
                if(N//i != i) and (N//i != temp):
                    s += N//i
                    
        
        if(s==temp):
            return 1
        return 0