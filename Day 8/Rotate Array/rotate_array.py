class Solution:
    
    def reverseArr(self,A,start,end):
        while start < end:
            A[start], A[end] = A[end], A[start]
            start += 1
            end += -1
            
    def rotateArr(self,A,D,N):
        D = D % N
        self.reverseArr(A, 0, D-1)
        self.reverseArr(A, D, N-1)
        self.reverseArr(A, 0, N-1)