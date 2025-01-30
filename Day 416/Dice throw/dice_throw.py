class Solution:
    def throw_dice(self, M, N, X, mem):
        if N == 0 and X == 0:
            mem[N][X] = 1
            return mem[N][X]
        if N == 0 and X > 0:
            mem[N][X] = 0
            return mem[N][X]
        if mem[N][X] != -1:
            return mem[N][X]
        cnt = 0
        for i in range(1, M+1):
            if X >= i:
                cnt += self.throw_dice(M, N-1, X-i, mem)
        mem[N][X] = cnt
        return mem[N][X]
        
    def noOfWays(self, m,n,x):
        mem = [[-1]*(X+1) for i in range(N+1)]
        return self.throw_dice(M, N, X, mem)