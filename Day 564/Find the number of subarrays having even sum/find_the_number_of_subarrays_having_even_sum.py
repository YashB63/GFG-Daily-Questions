class Solution:
    def countEvenSum(self, arr):
        n = len(arr)
        temp = [1, 0]  

        result = 0
        sum_val = 0

        for i in range(n):
            sum_val = (sum_val + arr[i]) % 2

            temp[sum_val] += 1

        result += (temp[0] * (temp[0] - 1) // 2)
        result += (temp[1] * (temp[1] - 1) // 2)

        return result