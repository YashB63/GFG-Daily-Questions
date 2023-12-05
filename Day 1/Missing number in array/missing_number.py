class Solution:
    def missingNumber(self,array,n):
        tot_sum = (n * (n + 1)) // 2
        arr_sum = sum(array)
        
        return tot_sum - arr_sum