class Solution:
    def rightmostNonZeroDigit (self, N, A):
        c2 = 0
        c5 = 0
        result = 1
        for num in A:
            if num == 0:
                return -1
            while num%2 == 0:
                c2 += 1
                num = num//2
            
            while num%5 == 0:
                c5 += 1
                num = num//5
            
            result = (result * num)%10
        
        ex2 = c2-c5
        
        if ex2>0:
            return result * (2**ex2) %10
        elif ex2<0:
            return result * (5**abs(ex2)) %10
        return result