class Solution:
    def sumMatrix(self, n, q):
        
        if q > 1 and q <= 2*n:
            if q < n-1:
                return q-1
            else:
                return 2*n+1-q
        else:
            return 0