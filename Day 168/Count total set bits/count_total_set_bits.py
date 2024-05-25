class Solution:
    
    def log(self, x):

        y = -1
        
        while x:
            x = x // 2
            y += 1
    
        return y
    def countSetBits(self,n):
    
        if n == 1:
            return 1
        if n == 0:
            return 0
    
        y = self.log(n)
    
        return y * 2 ** (y - 1) + n - 2**y + 1 + self.countSetBits(n - 2**y)