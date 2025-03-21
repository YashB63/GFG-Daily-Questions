class Solution:
    def mergeThree(self, A,B,C):
        A.extend(B)
        A.extend(C)
        A.sort()
        return A