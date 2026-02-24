import math

class Solution:
    def nthPosition (self, n):
        return 2**(int(math.log(n,2)))