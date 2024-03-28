class Solution:
    def series(self, n):
        
        x=[0]*(n+1)
        x[1]=1
        for i in range(2,n+1):
            x[i]=(x[i-1]+x[i-2])%(10**9+7)
        return x