class Solution:

    def sameChar(self, A, B):
        
        s=0
        A=A.lower()
        B=B.lower()
        for i in range(len(A)):
            if A[i]==B[i]:
                s+=1
        return s