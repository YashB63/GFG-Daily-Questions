class Solution:
    def leastPrimeFactor (self, n):
        
        x = [i for i in range(n+1)]
        x[1] = 1
        y = 2
        
        while y*y <= n:
            if x[y] == y:
                for i in range(y * y, n+1, y):
                    if x[i] == i:
                        x[i] = y
            
            y += 1
            
        return x