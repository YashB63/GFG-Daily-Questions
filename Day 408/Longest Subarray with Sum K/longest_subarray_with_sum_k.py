class Solution:
    def longestSubarray(self, arr, k):  
        m = {}
        m[0] = -1
        cur = 0
        ans = 0
        for i in range(len(arr)):
            cur+=arr[i]
            if cur-k in m:
                ans = max(ans,i-m[cur-k])
            if cur not in m: m[cur] = i
        return ans