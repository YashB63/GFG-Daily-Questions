class Solution:
    def shortestPath(self, x, y): 
        d = 0
        while x!=y:
            if x>y:
                x //= 2
            else:
                y //= 2
            d += 1
        return d