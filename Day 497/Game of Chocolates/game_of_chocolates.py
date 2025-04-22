import math

class Solution:
    def game(self, a, b):
        if a>=b:
            a,b=b,a
        k=b-a
        gold=(1+math.sqrt(5))/2
        c=int(k*gold)
        
        return False if a==c else True