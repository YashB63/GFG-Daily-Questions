import math

class Solution:
    def cuts(self, s):
        for i in range(22, -1, -1):
            s = s.replace(bin(int(math.pow(5, i)))[2:], "#")
        return -1 if "0" in s else len(s)