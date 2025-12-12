class Solution:
    def totalCost(self, mask, curr, cost, dp):
        n = len(cost)

        if mask == (1 << n) - 1:
            return cost[curr][0]

        if dp[curr][mask] != -1:
            return dp[curr][mask]

        ans = float('inf')

        for i in range(n):
            if (mask & (1 << i)) == 0:
                ans = min(
                    ans, cost[curr][i] +
                    self.totalCost(mask | (1 << i), i, cost, dp))

        dp[curr][mask] = ans
        return ans

    def tsp(self, cost):
        n = len(cost)
        dp = [[-1] * (1 << n) for _ in range(n)]

        for i in range(n):
            dp[i] = [-1] * (1 << n)

        mask = 1
        pos = 0

        return self.totalCost(mask, pos, cost, dp)