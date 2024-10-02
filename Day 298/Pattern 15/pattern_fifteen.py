class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            for j in range(65,65+N-i+1):
                print(chr(j),end = "")
            print(end = "\n")