class Solution:
    def printTriangle(self, N):
        for i in range(N):
            print(" " * i + "*" * (2*(N-i)-1))