class Solution:
    def subarrayXor(self, arr):
        result = 0
        n = len(arr)

        for i in range(n):
            if (i + 1) % 2 != 0 and (n - i) % 2 != 0:
                result ^= arr[i]

        return result