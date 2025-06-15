class Solution:
    def modpow(self, a, b, c):
        ans = 1
        while b != 0:
            if b % 2 == 1:
                ans = (ans * a) % c
            a = (a * a) % c
            b //= 2
        return ans

    def bnry(self, newrank, low, high, val):
        mid = (low + high) // 2

        if high == low + 1:
            return high

        if newrank[mid] > val:
            return self.bnry(newrank, low, mid, val)
        elif newrank[mid] < val:
            return self.bnry(newrank, mid, high, val)
        else:
            return mid

    def getTestMarks(self, n, q, r, l, rank, StoreAnswer):
        newrank = [0] * (n + 5)
    
        newrank[1] = r[1]
    
        for i in range(2, n + 1):
            newrank[i] = r[i] - (l[i] - newrank[i - 1] - 1)
    
        newrank[0] = 0
    
        for i in range(1, q + 1):
            val1 = self.bnry(newrank, 0, n, rank[i])
            ans = newrank[val1] - rank[i]
            StoreAnswer[i] = r[val1] - ans