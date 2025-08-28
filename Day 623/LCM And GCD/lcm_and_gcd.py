class Solution:
    def lcmAndGcd(self, a, b):
        arr = [0] * 2
        g = math.gcd(a, b) 
        l = (
            a * b
        ) // g  
        arr[0], arr[1] = l, g

        return arr