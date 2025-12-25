from itertools import permutations as perms

class Solution:
    def permutation(self,s):
        return sorted(["".join(x) for x in perms(list(s))])