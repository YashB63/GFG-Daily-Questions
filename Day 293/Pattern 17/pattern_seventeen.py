class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            print((N-i)*" ", end="") 
            for j in range (65,65+i):
                print(chr(j), end="") 
            for k in range (i-1, 0,-1):
                print(chr(64+k),end="")
            print("")