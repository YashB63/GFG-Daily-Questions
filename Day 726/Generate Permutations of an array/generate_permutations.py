from itertools import permutations as pr

class Solution:
    def permuteDist(self, arr):
        return list(pr(arr))