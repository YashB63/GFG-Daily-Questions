from math import log, ceil

class Solution:
    def baseEquiv(self, n, m):
        if self.check(n, m):
            return "Yes"
        return "No"

    def checkUtil(self, num, dig, base):
        if dig == 1 and num < base:
            return True
        if dig > 1 and num >= base:
            return self.checkUtil(num // base, dig - 1, base)
        return False

    def check(self, num, dig):
        for base in range(2, 33):
            if self.checkUtil(num, dig, base):
                return True
        return False