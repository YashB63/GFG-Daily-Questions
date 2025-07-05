class Solution:
    def countLessEq(self, a, b):
        n = len(a)
        m = len(b)

        res = [0] * n
        maxi = max(b)
        
        cnt = [0] * (maxi + 1)

        for i in range(m):
            cnt[b[i]] += 1

        for i in range(1, (maxi + 1)):
            cnt[i] += cnt[i - 1]

        for i in range(n):
            res[i] = cnt[min(a[i], maxi)]

        return res