class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        prefix_sum = 0
        max_len = 0
        seen = {}  

        for i in range(n):
            if arr[i] > k:
                prefix_sum += 1
            else:
                prefix_sum -= 1

            if prefix_sum > 0:
                max_len = i + 1  
            else:
                if (prefix_sum - 1) in seen:
                    max_len = max(max_len, i - seen[prefix_sum - 1])
            
            if prefix_sum not in seen:
                seen[prefix_sum] = i

        return max_len