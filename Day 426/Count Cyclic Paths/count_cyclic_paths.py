class Solution:
    def countPaths (self, N):
        mod=10**9+7
        up=1
        dw=0
        for _ in range(N):
            tup=up
            tdw=dw
            up=(3*tdw)%mod
            dw=(2*tdw+tup)%mod
            tup=up
            tdw=dw
        return up