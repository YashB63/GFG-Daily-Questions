class Solution:
    def maxChocolate(self, grid):
        from functools import lru_cache

        n = len(grid)
        m = len(grid[0]) if n > 0 else 0

        @lru_cache(None)
        def dp(i, j1, j2):
            if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
                return float('-inf')

            if i == n - 1:
                return grid[i][j1] if j1 == j2 else grid[i][j1] + grid[i][j2]

            best = float('-inf')
            curr_pick = grid[i][j1] if j1 == j2 else grid[i][j1] + grid[i][j2]

            for dj1 in (-1, 0, 1):
                for dj2 in (-1, 0, 1):
                    best = max(best, curr_pick + dp(i + 1, j1 + dj1, j2 + dj2))

            return best

        return dp(0, 0, m - 1)