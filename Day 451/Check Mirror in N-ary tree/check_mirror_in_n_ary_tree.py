from collections import defaultdict

class Solution:
    def checkMirrorTree(self, n, e, A, B):
        if len(A) != len(B):
            return 0
            
        tree_A = defaultdict(list)
        tree_B = defaultdict(list)
        
        for i in range(0, 2*e, 2):
            tree_A[A[i]].append(A[i + 1])
            tree_B[B[i]].append(B[i + 1])
            
        for node in tree_A:
            
            if tree_A[node] != tree_B[node][::-1]:
                return 0
                
        return 1