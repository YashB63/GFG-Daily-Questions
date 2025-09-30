class Solution:
    def getOddOccurrence(self, arr):
        xor = arr[0]
        n = len(arr)

        for i in range(1, n):
            xor ^= arr[i]

        return xor