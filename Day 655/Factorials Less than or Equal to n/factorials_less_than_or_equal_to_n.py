class Solution:
    def factorialNumbers(self, n):
        fac = 1  
        x = 2  
        ans = []  
        while fac <= n:  
            ans.append(fac)  
            fac *= x  
            x += 1  
        return ans