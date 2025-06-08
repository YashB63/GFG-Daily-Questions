class Solution:
    def minSwaps(self, arr):
        n = len(arr)  

        noOfOnes = sum(arr)  

        if noOfOnes == 0:
            return -1

        x = noOfOnes

        maxOnes = float('-inf')

        preCompute = [0] * n

        if arr[0] == 1:
            preCompute[0] = 1
        for i in range(1, n):
            preCompute[i] = preCompute[i - 1] + (1 if arr[i] == 1 else 0)

        for i in range(x - 1, n):
            if i == (x - 1):
                noOfOnes = preCompute[i]
            else:
                noOfOnes = preCompute[i] - preCompute[i - x]

            maxOnes = max(maxOnes, noOfOnes)

        noOfZeroes = x - maxOnes

        return noOfZeroes