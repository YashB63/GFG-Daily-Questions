class Solution:
    def minCandy(self, N, ratings):
        
        if N == 0:
            return 0
        c = [1 for _ in range(N)]
        for i in range(1, N):
            if ratings[i] > ratings[i-1]:
                c[i] = c[i - 1] + 1
        for i in range(N - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                c[i] = max(c[i], c[i + 1] + 1)
        return sum(c)