class Solution:
    def productExceptSelf(self, arr):
        n = len(arr)
        res = [1] * n

        prefix_product = 1
        for i in range(n):
            res[i] = prefix_product
            prefix_product *= arr[i]

        suffix_product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix_product
            suffix_product *= arr[i]

        return res