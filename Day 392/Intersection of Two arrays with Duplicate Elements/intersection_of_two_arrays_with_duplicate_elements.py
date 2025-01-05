class Solution:
    def intersectionWithDuplicates(self, a, b):
        res1 = set(a)
        res2 = set(b)
        result = list(res1.intersection(res2))
        return result