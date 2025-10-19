class Solution:
    def combinationSum(self, n, k):
        def findCombinations(n, k, subVector, res, last):
            if n == 0 and k == 0:
                res.append(subVector[:])
                return

            if n < 0 or k < 0:
                return

            for i in range(last, 10):
                subVector.append(i)
                findCombinations(n - i, k - 1, subVector, res, i + 1)

                subVector.pop()

        if n < k or n > 9 * k:
            return []

        res = []
        findCombinations(n, k, [], res, 1)
        return res