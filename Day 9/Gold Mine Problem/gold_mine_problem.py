class Solution:
    def maxGold(self, n, m, M):
        dp = [[0 for _ in range(m)] for _ in range(n)]
        
        for col in range(m - 1, -1, -1):
            for row in range(n):
                right = 0 if col == m - 1 else dp[row][col + 1]
                right_up = 0 if row == 0 or col == m - 1 else dp[row - 1][col + 1]
                right_down = 0 if row == n - 1 or col == m - 1 else dp[row + 1][col + 1]
                
                dp[row][col] = M[row][col] + max(right, right_up, right_down)
                
        max_gold = 0
        for i in range(n):
            max_gold = max(max_gold, dp[i][0])
            
        return max_gold