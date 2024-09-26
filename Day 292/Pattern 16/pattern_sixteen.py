class Solution:
    def printTriangle(self, N):
        n = N
        for i in range(n):
            for j in range(i+1):
                print(chr(65 + i), end="")
            print()