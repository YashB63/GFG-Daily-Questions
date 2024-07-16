from typing import List

class Solution:
    def maxSquare(self, n : int, m : int, mat : List[List[int]]) -> int:
        mx=0
        dp=[[0]*(m+1) for _ in range(n+1)]
        for y in range(1,n+1):
            for x in range(1,m+1):
                if mat[y-1][x-1]==1:
                    dp[y][x]=min(dp[y-1][x],dp[y][x-1],dp[y-1][x-1])+1
                    mx=max(mx,dp[y][x])
        return mx