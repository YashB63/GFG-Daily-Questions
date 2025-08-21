class Solution:
    def minSoldiers(self, arr, k):
        n = len(arr)
        need = (n + 1) // 2
        costs = []

        for num in arr:
            if num % k == 0:
                costs.append(0)
            else:
                costs.append(k - (num % k))

        costs.sort()

        total = sum(costs[:need])

        return total