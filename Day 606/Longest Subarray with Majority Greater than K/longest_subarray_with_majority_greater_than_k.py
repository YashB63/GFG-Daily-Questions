class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        mp = {}
        ans = 0
        total = 0  

        for i in range(n):
            if arr[i] <= k:
                total -= 1
            else:
                total += 1

            if total > 0:
                ans = i + 1
            else:
                if (total - 1) in mp:
                    ans = max(ans, i - mp[total - 1])

            if total not in mp:
                mp[total] = i

        return ans