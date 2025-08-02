class Solution:
    def maxCalories(self, Arr, n):
        if n == 0:
            return 0

        sum_arr = [0] * n

        if n >= 1:
            sum_arr[0] = Arr[0]

        if n >= 2:
            sum_arr[1] = Arr[0] + Arr[1]

        if n > 2:
            sum_arr[2] = max(sum_arr[1], max(Arr[1] + Arr[2], Arr[0] + Arr[2]))

        for i in range(3, n):
            sum_arr[i] = max(
                sum_arr[i - 1],                          
                sum_arr[i - 2] + Arr[i],                 
                Arr[i] + Arr[i - 1] + sum_arr[i - 3]     
            )

        return sum_arr[n - 1]