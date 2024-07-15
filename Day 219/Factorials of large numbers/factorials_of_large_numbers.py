import math

class Solution:
    def factorial(self, N):
        fact = math.factorial(N)
        digits = [int(digit) for digit in str(fact)]
    
        return digits