class Solution:
    def maxZero(self, arr):
        maxZeros = 0
        res = '-1'
        for number in arr:
            zeros = 0
            for digit in number:
                if digit == '0':
                    zeros += 1
            if maxZeros < zeros:
                maxZeros = zeros
                res = number
            if maxZeros != 0:
                if maxZeros == zeros:
                    if len(res) == len(number) and res < number:
                        res = number
                    elif len(res) < len(number):
                        res = number
        return res