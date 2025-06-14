class Solution:
    def longestCommonSum(self, arr1, arr2):
        n = len(arr1)
        res = 0

        diffMap = {}

        sum1 = 0
        sum2 = 0

        for i in range(n):
            sum1 += arr1[i]
            sum2 += arr2[i]

            currentDiff = sum1 - sum2

            if currentDiff == 0:
                res = max(res, i + 1)

            elif currentDiff in diffMap:
                res = max(res, i - diffMap[currentDiff])
            else:
                diffMap[currentDiff] = i

        return res