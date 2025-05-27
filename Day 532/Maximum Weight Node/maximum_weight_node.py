class Solution:
    def maxWeightCell(self, exits):
        n = len(exits)
        weight = [0] * n

        for i in range(n):
            if (exits[i] != -1):
                weight[exits[i]] += i

        ans = [-1, -1]

        for i in range(n):
            ans = max(ans, [weight[i], i])

        return ans[1]