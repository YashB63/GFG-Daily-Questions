from typing import List

class Solution:
    def makeChanges(self, N : int, k : int, target : int, coins : List[int]) -> bool:
        dp = [[False] * (target + 1) for _ in range(k + 1)]  
        dp[0][0] = True  
        for i in range(1, k + 1):  
            for j in range(1, target + 1):  
                for l in coins:  
                    if j < l:  
                        continue
                    dp[i][j] |= dp[i - 1][j - l]  
        return dp[k][target]