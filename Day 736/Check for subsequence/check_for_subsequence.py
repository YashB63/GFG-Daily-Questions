class Solution:
    def isSubSequence(self, A, B):
        for i in range(len(A)):
            if A[i] in B:
                B = B[(B.index(A[i])) + 1 :]
            else:
                return 0
        return 1