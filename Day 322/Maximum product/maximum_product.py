class Solution:
    def maxProductSubarrayOfSizeK(self, arr, k):
        product = 1
        arr.sort()
        if k % 2 and arr[-1] < 0:
            for _ in range(k):
                product *= arr.pop()
            return product
        if k % 2:
            product *= arr.pop()
            k -= 1
        while k:
            if arr[0] * arr[1] > arr[-1] * arr[-2]:
                product *= arr.pop(0) * arr.pop(0)
            else:
                product *= arr.pop() * arr.pop()
            k -= 2
            
        return product