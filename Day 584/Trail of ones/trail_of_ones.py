class Solution:
    def countConsec(self, n: int) -> int:
        prev0, prev1 = 0, 0

        for i in range(n, 0, -1):
            curr0 = prev0 + prev1

            curr1 = prev0 + (1 << (n - i))

            prev0, prev1 = curr0, curr1

        return prev0