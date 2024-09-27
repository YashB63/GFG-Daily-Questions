class Solution:
    def printTriangle(self, N):
        for i in range(N,0,-1):
            print("*"*(i)+" "*((N*2)-(i*2))+"*"*(i),end='\n')
            
        for i in range(1,N+1):
            print("*"*(i)+" "*((N*2)-(i*2))+"*"*(i),end='\n')