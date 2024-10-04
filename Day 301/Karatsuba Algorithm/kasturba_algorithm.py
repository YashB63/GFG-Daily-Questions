class Solution:
    def karatsubaAlgo(self, x, y):
        x = int(x, 2)
        y = int(y, 2)
        return self.karatsuba(x, y)
        
    def karatsuba(self,x, y):
        if x < 10 or y < 10:
            return x * y
        
        n = max(len(str(x)), len(str(y)))
        half = n // 2
    
        x1 = x // (10 ** half)
        x0 = x % (10 ** half)
        y1 = y // (10 ** half)
        y0 = y % (10 ** half)
        
        z2 = self.karatsuba(x1, y1)
        z0 = self.karatsuba(x0, y0)
        z1 = self.karatsuba((x0 + x1), (y0 + y1)) - z2 - z0
    
        return (z2 * 10**(2*half)) + (z1 * 10**half) + z0