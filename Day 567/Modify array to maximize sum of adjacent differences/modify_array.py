import sys

sys.setrecursionlimit(10**6)
dp = [[0] * 2 for i in range(10**5 + 1)]

class Solution:
    def maximumDifferenceSum(self, arr, N):
        global dp
        
        for i in range(N + 1):
            for j in range(2):
                dp[i][j] = -1
        
        x = self.solve(arr, 1, N, 0)
        y = self.solve(arr, 1, N, 1)
        
        return max(x, y)

    
    def solve(self, arr, i, n, x):
        global dp
        if i == n:
            return 0
        
        if dp[i][x] != -1:
            return dp[i][x]
        
        if x == 0:
            op1 = abs(arr[i] - arr[i - 1]) + self.solve(arr, i + 1, n, 0)
            op2 = abs(1 - arr[i - 1]) + self.solve(arr, i + 1, n, 1)
            dp[i][x] = max(op1, op2)
            return dp[i][x]

        else:
            op1 = abs(arr[i] - 1) + self.solve(arr, i + 1, n, 0)
            op2 = self.solve(arr, i + 1, n, 1)
            dp[i][x] = max(op1, op2)
            return dp[i][x]