class Solution:
    def getCommon(self, arr1, arr2):
        lcslen = [[0 for i in range(12)] for j in range(12)]

        for i in range(0, 10):
            for j in range(0, 10):
                if (arr1[i] == arr2[j]):
                    lcslen[i + 1][j + 1] = 1 + lcslen[i][j]
                else:
                    lcslen[i + 1][j + 1] = max(lcslen[i + 1][j],
                                               lcslen[i][j + 1])

        return lcslen[10][10]