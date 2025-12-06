class Solution:
    def subsetXORSum(self, arr):
        result = 0
        for num in arr:
            result |= num
        return result << (len(arr) - 1)