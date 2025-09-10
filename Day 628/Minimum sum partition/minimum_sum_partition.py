class Solution:
    def minDifference(self, arr):
        total = sum(arr)
        possible = [False] * (total + 1)
        possible[0] = True

        for a in arr:
            for s in range(total, a - 1, -1):
                if possible[s - a]:
                    possible[s] = True

        for s in range(total // 2, -1, -1):
            if possible[s]:
                return total - 2 * s