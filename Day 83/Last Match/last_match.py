class Solution:
    def findLastOccurence(self, A, B):
        
        a = len(A)
        b = len(B)
        last_index = -1
        
        for i in range(a - b + 1):
            j = 0
            while j < b and A[i + j] == B[j]:
                j += 1
                
            if j == b:
                last_index = i + 1
                
        return last_index