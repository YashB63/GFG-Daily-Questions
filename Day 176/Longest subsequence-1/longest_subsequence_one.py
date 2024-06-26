from typing import List

class Solution:
    def longestSubseq(self, n : int, a : List[int]) -> int:
        
        dp = [1]*n
        ans = 1
        for i in range(1, n):
            for j in range(i):
                if abs(a[i]-a[j]) == 1:
                    dp[i] = max(dp[i], dp[j]+1)
                    ans = max(ans, dp[i])
        return ans