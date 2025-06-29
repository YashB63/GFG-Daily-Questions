class Solution:
    def lds(self, arr, memo, parent, i):
        if memo[i] != -1:
            return memo[i]
        maxLength = 1
        bestParent = -1

        for j in range(i):
            if arr[j] % arr[i] == 0:
                length = self.lds(arr, memo, parent, j) + 1
                if length > maxLength:
                    maxLength = length
                    bestParent = j

        memo[i] = maxLength
        parent[i] = bestParent
        return maxLength

    def largestSubset(self, arr):
        n = len(arr)
        arr.sort(reverse=True)  

        memo = [-1] * n
        parent = [-1] * n

        maxSize = 0
        lastIndex = 0

        for i in range(n):
            size = self.lds(arr, memo, parent, i)
            if size > maxSize:
                maxSize = size
                lastIndex = i

        res = []
        i = lastIndex
        while i != -1:
            res.append(arr[i])
            i = parent[i]

        return res