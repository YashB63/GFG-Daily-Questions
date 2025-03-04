from itertools import permutations

class Solution:
    def findRank(self,s):
        realstr = sorted(s)
        count = 0
        for p in permutations(realstr):
            if(''.join(p)==s):
                count +=1
                return count
            count +=1