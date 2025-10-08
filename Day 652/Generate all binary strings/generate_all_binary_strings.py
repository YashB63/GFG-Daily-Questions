class Solution:
    def binstr(self, n):
        res = []
        for i in range(1 << n):
            s = ''.join('1' if (i >> j) & 1 else '0' for j in reversed(range(n)))
            res.append(s)
        return res