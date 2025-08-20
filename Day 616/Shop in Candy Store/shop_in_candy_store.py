class Solution:
    def minMaxCandy(self, prices, k):
        prices.sort()
        n = len(prices)

        minCost = 0
        i = 0
        remaining = n
        while i < remaining:
            minCost += prices[i]
            i += 1
            remaining -= k

        maxCost = 0
        i = n - 1
        index = -1
        while i > index:
            maxCost += prices[i]
            i -= 1
            index += k

        return [minCost, maxCost]