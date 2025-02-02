class Solution:
    def transfigure(self, A, B): 
        if len(A) != len(B):
            return -1
            
        for c in set(A):
            if A.count(c) != B.count(c):
                return -1
                
        count=0
        i=len(A)-1
        j=len(B)-1
        while i>=0 and j>=0:
    
            if A[i]==B[j]:
                i-=1
                j-=1
            else:
                i-=1
                count+=1
                
        if count==len(A) :
            return -1
        else:
            return count