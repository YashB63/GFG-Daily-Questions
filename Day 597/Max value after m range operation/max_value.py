class Solution:
    def find_max(self, n, a, b, k):
        arr = [0] * (n + 1)  

        m = len(a)

        for i in range(m):
            lowerbound = a[i]
            upperbound = b[i]

            arr[lowerbound] += k[i]

            if upperbound + 1 < n:
                arr[upperbound + 1] -= k[i]

        sum_value = 0
        res = float('-inf')

        for i in range(n):
            sum_value += arr[i]
            res = max(res, sum_value)

        return res