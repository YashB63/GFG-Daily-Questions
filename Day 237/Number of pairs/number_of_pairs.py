class Solution:
    def countPairs(self,a,b,M,N):
        x = [i ** (1/i) for i in a]
        y = [i ** (1/i) for i in b]
        y.sort()
        x.sort()
        cnt = 0
        j = 0
        for i in range(M):
            while j < N and x[i] > y[j]:
                j += 1
            cnt += j
        return cnt