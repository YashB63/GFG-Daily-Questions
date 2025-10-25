class Solution:
    def min_value_to_balance(self, arr):
        n = len(arr)
        sum1 = sum(arr[:n // 2])  
        sum2 = sum(arr[n // 2:])  
        return abs(sum1 -
                   sum2)