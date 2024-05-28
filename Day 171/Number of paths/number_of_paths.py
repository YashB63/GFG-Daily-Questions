class Solution:
    mod=10**9+7
    def numberOfPaths (self, M, N):
        
        n=M+N-2
        r=min(M-1,N-1)
        num,deno=1,1
        for i in range(1,r+1):
            num*=(n+1-i)
            deno*=i
        return (num//deno)%self.mod