class Solution:
    def maxMinProduct(self, arr):
        n = len(arr)
        if n == 0:
            return [0, 0]  

        curMaxProduct = arr[0]
        curMinProduct = arr[0]
        prevMaxProduct = arr[0]
        prevMinProduct = arr[0]
        maxProduct = arr[0]
        minProduct = arr[0]

        for i in range(1, n):
            curMaxProduct = max(prevMaxProduct * arr[i],
                                max(prevMinProduct * arr[i], arr[i]))
            curMaxProduct = max(curMaxProduct, prevMaxProduct)
            curMinProduct = min(prevMaxProduct * arr[i],
                                min(prevMinProduct * arr[i], arr[i]))
            curMinProduct = min(curMinProduct, prevMinProduct)

            maxProduct = max(maxProduct, curMaxProduct)
            minProduct = min(minProduct, curMinProduct)

            prevMaxProduct = curMaxProduct
            prevMinProduct = curMinProduct

        return [maxProduct, minProduct]