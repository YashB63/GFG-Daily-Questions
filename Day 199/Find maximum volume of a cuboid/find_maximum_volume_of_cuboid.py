class Solution:
    def maxVolume(self, p, a):
        
        l = (p - math.sqrt(p * p - 24 * a)) / 12
        
        h = (p / 4) - (2 * l)
        v = l * l * h
        return round(v, 2)