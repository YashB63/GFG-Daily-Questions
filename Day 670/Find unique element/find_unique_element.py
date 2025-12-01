class Solution:

    def find_unique(self, k, arr):
        INT_SIZE = 8 * 4  
        count = [0] * INT_SIZE

        n = len(arr)

        for i in range(INT_SIZE):
            for j in range(n):
                if (arr[j] & (1 << i)) != 0:
                    count[i] += 1

        res = 0
        for i in range(INT_SIZE):
            res += (count[i] % k) * (1 << i)

        return res