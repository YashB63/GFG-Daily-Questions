class Solution:
    def distinctSubseq(self, str):
        n = len(s)
        MOD = 10**9 + 7

        last = [0] * 26

        res = 1

        for i in range(1, n + 1):
            idx = ord(s[i - 1]) - ord('a')
            cur = (2 * res - last[idx]) % MOD

            last[idx] = res
            res = cur

        return res