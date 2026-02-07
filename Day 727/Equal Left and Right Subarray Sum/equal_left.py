class Solution:
    def equalSum(self, arr):
        N = len(arr)
        
        sum = 0
        for i in range(0, N):
            sum += arr[i]

        sum2 = 0

        for i in range(0, N, +1):
            sum -= arr[i]

            if sum2 == sum:
                return (i)

            sum2 += arr[i]

        return -1