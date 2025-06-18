class Solution:
    def DivCountSum(self, n):
        result_sum = 0
        for i in range(1, n + 1):
            result_sum += n // i
        return result_sum