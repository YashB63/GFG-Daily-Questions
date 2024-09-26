class Solution:
    def printTriangle(self, N):
        for i in range(1, N+1):
            for num in range(1, i+1):
                print(num, end = " ")
                
            for s in range(i+1, 2*N-i+1):
                print("  ", end ="")
                
            for num in range(2*N-i, 2*N):
                print(2*N-num, end = " ")
                
            print()