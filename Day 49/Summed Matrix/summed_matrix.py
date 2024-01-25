class Solution:
    def sumMatrix(self, n, q):
         
        if q <= (n + 1):
            count = (q-1)
        else:
            count = 2 * n - q + 1
        
        if count < 0:
            count = 0
        
        return count