class Solution:
    def getLastDigit(self, a, b):
        if b == '0':
            return 1
        last=int(a[-1])
        exp=int(b)
        return pow(last,exp,10)