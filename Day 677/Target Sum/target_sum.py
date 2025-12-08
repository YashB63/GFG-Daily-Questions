from functools import lru_cache
import sys 
sys.setrecursionlimit(10**7)
class Solution:
    def findTargetSumWays(self, n, arr, target):
        mod = 10**9+7
        @lru_cache(None)
        def dp(i,target):
            if i==n:
                if target==0:
                    return 1
                return 0
            return (dp(i+1,target-arr[i]) + dp(i+1,target+arr[i]))%mod
        return dp(0,target)