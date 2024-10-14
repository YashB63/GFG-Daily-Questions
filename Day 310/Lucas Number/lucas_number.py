class Solution:
    def lucas(self, n):
        a = 2
        b = 1
        for i in range(2, n+1):
            c = (a+b)%1000000007
            a = b
            b = c
        return b