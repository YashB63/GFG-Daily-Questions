class Solution:
    def minFind(self, n, a):
        R = 0
        G = 0
        B = 0
        
        for j in range(n):
            if a[j] == 'R':
                R += 1
            elif a[j] == 'G':
                G += 1
            else:
                B += 1
        
        if R and (G == 0 and B == 0):
            return n
        elif G and (R == 0 and B == 0):
            return n
        elif B and (R == 0 and G == 0):
            return n
            
        if R%2 == 0 and B%2 == 0 and G%2 == 0:
            return 2
            
        if R%2 == 1 and B%2 == 1 and G%2 == 1:
            return 2
            
        return 1