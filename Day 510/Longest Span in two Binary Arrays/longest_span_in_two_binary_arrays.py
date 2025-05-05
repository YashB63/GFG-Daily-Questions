class Solution:
    def longestCommonSum(self, arr1, arr2):
        n = len(arr1)
        
        diff = [arr1[i] - arr2[i] for i in range(n)]

        prefix_sum = 0
        max_length = 0
        sum_index_map = {0: -1}  

        for i in range(n):
            prefix_sum += diff[i]

            if prefix_sum in sum_index_map:
                max_length = max(max_length, i - sum_index_map[prefix_sum])
            else:
                sum_index_map[prefix_sum] = i  

        return max_length