class Solution:
    def findXOR(self, l, r):
        def xor_1_to_N(n):
            if n%4==0:
                return n
            if n%4==1:
                return 1
            if n%4==2:
                return n+1
            if n%4==3:
                return 0
        return xor_1_to_N(l-1)^xor_1_to_N(r)