from itertools import permutations
class Solution:
    def uniquePerms(self, arr, n):
         
        x = set(permutations(arr))
        res = [list(perm) for perm in x]
        res.sort()
        return res