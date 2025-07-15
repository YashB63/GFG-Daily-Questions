class Solution:
    def findGreater(self, arr):
        n = len(arr)
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        res = [-1] * n
        s = []

        for i in range(n):
            while s and freq[arr[i]] > freq[arr[s[-1]]]:
                res[s.pop()] = arr[i]
            s.append(i)

        return res