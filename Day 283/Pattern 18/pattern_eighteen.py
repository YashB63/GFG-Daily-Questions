class Solution:
    def printTriangle(self, N):
        for row in range(N,0,-1):
            for col in range(N,row-1,-1):
                print(chr(col+64),end=" ")
            print()