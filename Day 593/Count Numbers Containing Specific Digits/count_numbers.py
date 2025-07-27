class Solution:
    def fastpow(self, base, exp):
        result = 1
        while exp > 0:
            if exp & 1:
                result *= base
            base *= base
            exp >>= 1
        return result

    def countValid(self, n, arr):
        good = [False] * 10
        for d in arr:
            good[d] = True

        f = 0
        f0 = 0
        for d in range(10):
            if not good[d]:
                f += 1
                if d != 0:
                    f0 += 1

        total = 9 * self.fastpow(10, n - 1)

        none_allowed = f0 if n == 1 else f0 * self.fastpow(f, n - 1)

        return total - none_allowed