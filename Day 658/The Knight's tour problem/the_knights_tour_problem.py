class Solution:
    def dfs(self, i, j, n, ans, cnt):
        if cnt[0] == n * n:
            return True

        for r in range(i - 2, i + 3):
            for c in range(j - 2, j + 3):
                rDist = abs(r - i)
                cDist = abs(c - j)

                if 0 <= r < n and 0 <= c < n and ans[r][c] == -1 and rDist + cDist == 3:
                    ans[r][c] = ans[i][j] + 1
                    cnt[0] += 1
                    if self.dfs(r, c, n, ans, cnt):
                        return True
                    # Backtrack
                    ans[r][c] = -1
                    cnt[0] -= 1
        return False

    def knightTour(self, n):
        ans = [[-1 for _ in range(n)] for _ in range(n)]
        ans[0][0] = 0
        cnt = [1]  

        if self.dfs(0, 0, n, ans, cnt):
            return ans
        return []