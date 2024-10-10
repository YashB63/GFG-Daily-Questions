class Solution:
    def isHappy (self, n):
        def sqr(num):
            return sum(int(digit)**2 for digit in str(num))
        sn=set()
        while n!=1 and n not in sn:
            sn.add(n)
            n=sqr(n)
        if n==1:
            return 1
        return 0