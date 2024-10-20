class Solution:
    def leftCandies(self, n, m):
        total_per_round = int(((n)*(n+1))/2)
        left = m%total_per_round
        for i in range(1,n+1):
            if left<(i):
                break
            left-=(i)
        return left