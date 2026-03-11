from math import gcd

class Solution:
    def getSmallestDivNum(self, n): 
        lcm = 1
        for i in range(2,n+1):
            lcm = lcm*i//gcd(lcm, i)
        return lcm