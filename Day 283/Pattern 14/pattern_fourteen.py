class Solution:
    def printTriangle(self, N):
        for i in range(65,65+N):
            for j in range(65, i+1):
                print(chr(j), end = "")
            print()