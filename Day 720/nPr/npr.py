from math import factorial

class Solution:
    def nPr(self, n, r):
        return factorial(n)//factorial(n - r)