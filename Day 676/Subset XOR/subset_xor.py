class Solution:
    def subsetXOR(self, n: int):
        r = n % 4

        if r == 0:
            ans = list(range(1, n + 1))

        elif r == 2:
            ans = list(range(2, n + 1))

        elif r == 3:
            ans = list(range(1, n))

        else:
            ans = [i for i in range(1, n + 1) if i != n - 1]

        return ans