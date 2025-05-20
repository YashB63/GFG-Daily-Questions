class Solution:

    def nCr(self, n, r):
        if r > n:
            return 0

        sum = 1

        for i in range(1, r + 1):
            sum = sum * (n - r + i) // i

        return sum