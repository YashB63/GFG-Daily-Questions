from bisect import bisect_left, bisect_right

class Solution:
    def __init__(self):
        self.p = self.precompute()

    def solve(self, L, R):
        p = self.p
        low = bisect_left(p, L)
        high = bisect_right(p, R)
        return high - low

    def precompute(self):
        v = []
        for i in range(63):
            for j in range(i + 1, 63):
                for k in range(j + 1, 63):
                    v.append((1 << i) + (1 << j) + (1 << k))
        v.sort()
        return v