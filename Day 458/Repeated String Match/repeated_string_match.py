import math

class Solution:
    def repeatedStringMatch(self, a, b):
        minrep = math.ceil(len(b)/len(a))
        repa = a*minrep
        
        if b in repa:
            return minrep
        repa+=a
        if b in repa:
            return minrep+1
        return -1