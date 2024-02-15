class Solution:
    def recamanSequence(self, n):
        
        x = [0] * n
        y = set()
        
        for i in range(1,n):
            x[i] = x[i-1] - i
            
            if x[i] <= 0 or x[i] in y:
                x[i] = x[i-1] + i
                
            y.add(x[i])
            
        return x