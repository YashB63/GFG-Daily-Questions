from math import sqrt

class Solution:
    def rectanglesInCircle(self,r):
        
        co = 0
        maxr = (2 * r) ** 2
        
        for l in range(1, 2 * r + 1):
            maxw = int(math.sqrt(maxr - l**2))
            co += maxw
        
        return co