class Solution:
    def maxProduct(self, arr):
        max_val = 0

        second_max = 0
        n = len(arr)

        for i in range(n):
            if arr[i] >= max_val:
                second_max = max_val
                max_val = arr[i]
            
            elif arr[i] >= second_max:
                second_max = arr[i]

        return max_val * second_max