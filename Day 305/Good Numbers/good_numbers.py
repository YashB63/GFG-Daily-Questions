class Solution:
    def goodNumbers(self,L,R,D):
        def validate(n, D):
            prev = n % 10
            
            if prev == D:
                return False
                
            n = n // 10
            
            while n > 0:
                if n % 10 == D or n % 10 <= prev:
                    return False
                    
                prev = prev + (n % 10)
                n = n // 10
                
            return True
            
        res = []
        for i in range(L, R + 1):
            if validate(i, D):
                res.append(i)
                
        return res