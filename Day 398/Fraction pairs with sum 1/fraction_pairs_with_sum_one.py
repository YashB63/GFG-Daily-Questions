import math

class Solution:
    def countFractions(self, n, numerator, denominator):
        d={}
        count=0
        for i in range(n):
            x=numerator[i]
            y=denominator[i]
            lcm=math.gcd(x,y)
            x//=lcm
            y//=lcm
            want_x=y-x
            want_y=y
            if (want_x,want_y) in d:
                count+=d[(want_x,want_y)]
            if (x,y) in d:
                d[(x,y)]+=1
            else:
                d[(x,y)]=1
        return count