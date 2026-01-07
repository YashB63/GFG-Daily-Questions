import math

def seves(n):
    arr=[1]*(n+1)
    arr[0]=0
    arr[1]=0
    for i in range(2,int(math.sqrt(n))+1):
        if arr[i]==1:
            for i in range(i*i,n+1,i):
                arr[i]=0
    return arr
        
class Solution:        
    def primeRange(self,M,N):
        arr=seves(N)
        lis=[]
        for i in range(M,N+1):
            if arr[i]:
                lis.append(i)
        return lis