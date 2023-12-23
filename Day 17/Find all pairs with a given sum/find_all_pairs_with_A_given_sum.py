class Solution:
    def allPairs(self, A, B, N, M, X):
        
        arr = []
        A.sort()
        for i in A:
            if X-i in B:
                arr.append((i, X-i))
        return arr