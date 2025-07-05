class Solution:
    def toggleBits(self, n , l , r):
        res = n
        for i in range(l, r + 1):
            if ((n & (1 << (i - 1))) != 0):
                res = res ^ (1 << (i - 1))
     
            else:
                res = res | (1 << (i - 1))
     
        return res