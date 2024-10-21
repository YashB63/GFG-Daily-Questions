class Solution:
    def printTriangle(self, N):
        k=N*2-2
        for i in range(1,N+1):
            print("*"*i,end='')
            print(" "*k,end="")
            print("*"*i)
            k-=2
        k+=4
        for i in range(N-1,0,-1):
            print("*"*i,end="")
            print(" "*k,end="")
            print("*"*i)
            k+=2