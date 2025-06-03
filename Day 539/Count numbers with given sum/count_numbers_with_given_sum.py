class Solution:
    def countWays(self, n, total_sum):
        MOD = 1000000007
        prev = [0] * (total_sum + 1)

        for s in range(1, min(10, total_sum + 1)):
            prev[s] = 1

        for i in range(1, n):
            curr = [0] * (total_sum + 1)
            prefix = [0] * (total_sum + 2)

            for s in range(total_sum + 1):
                prefix[s + 1] = (prefix[s] + prev[s]) % MOD

            for s in range(total_sum + 1):
                l = max(0, s - 9)
                r = s
                curr[s] = (prefix[r + 1] - prefix[l] + MOD) % MOD

            prev = curr

        return -1 if prev[total_sum] == 0 else prev[total_sum]