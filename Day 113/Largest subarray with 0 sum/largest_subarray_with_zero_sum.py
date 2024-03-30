class Solution:
    def maxLen(self, n, arr):
        
        ans = 0
        prefix = {}
        pre_sum = 0
        prefix[0]=-1
        for i in range(n):
            pre_sum += arr[i]
            if pre_sum in prefix:
                ans = max(ans,i-prefix[pre_sum])
            else:
                prefix[pre_sum] = i
        return ans