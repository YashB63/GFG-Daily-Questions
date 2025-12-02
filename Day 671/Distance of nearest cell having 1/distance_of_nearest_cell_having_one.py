class Solution:
    def nearest(self, grid):
        n = len(grid)
        m = len(grid[0])

        ans = [[sys.maxsize for _ in range(m)] for _ in range(n)]

        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans[i][j] = 0
                    q.append((i, j))

        while q:
            len_q = len(q)

            for _ in range(len_q):
                x, y = q.popleft()

                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                for dx, dy in directions:
                    if 0 <= x + dx < n and 0 <= y + dy < m and ans[x + dx][
                            y + dy] == sys.maxsize:
                        ans[x + dx][y + dy] = ans[x][y] + 1
                        q.append((x + dx, y + dy))
        return ans