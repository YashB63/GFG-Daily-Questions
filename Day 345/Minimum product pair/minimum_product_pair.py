class Solution:
    def printMinimumProduct(self, a):
        A = sorted(a)
        return A[0]*A[1]