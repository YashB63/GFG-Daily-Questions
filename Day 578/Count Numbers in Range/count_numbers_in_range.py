import math

class Solution:
    def count3DivNums(self, L: int, R: int) -> int:
        composite = [False] * 31625
        dp = [0] * 31625

        composite[0] = composite[1] = True
        dp[0] = dp[1] = 0

        for i in range(2, 31625):
            dp[i] = dp[i - 1]
            if not composite[i]:
                dp[i] += 1
                for j in range(i * 2, 31625, i):
                    composite[j] = True

        prevL = L
        L = int(math.sqrt(L))
        if L * L < prevL:
            L += 1
        R = int(math.sqrt(R))

        ct = dp[R] - dp[L - 1]

        return ct