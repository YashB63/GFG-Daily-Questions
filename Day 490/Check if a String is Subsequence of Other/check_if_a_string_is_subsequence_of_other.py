class Solution:
    
    def isSubSequence(self, A, B):
        i, j = 0, 0
        len_A, len_B = len(A), len(B)

        while j < len_B:
            if i < len_A and A[i] == B[j]:  
                i += 1 
            j += 1  

            if i == len_A:  
                return True

        return False