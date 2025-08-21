class Solution:
    def floodFillUtil(self, screen, x, y, prevC, newC, N, M):
        if x < 0 or x >= N or y < 0 or y >= M:
            return
        if screen[x][y] != prevC:
            return

        screen[x][y] = newC
        self.floodFillUtil(screen, x + 1, y, prevC, newC, N, M)
        self.floodFillUtil(screen, x - 1, y, prevC, newC, N, M)
        self.floodFillUtil(screen, x, y + 1, prevC, newC, N, M)
        self.floodFillUtil(screen, x, y - 1, prevC, newC, N, M)

    def fill(self, mat):
        n = len(mat)
        m = len(mat[0])
        temp = []
        for i in range(n):
            row = []
            for j in range(m):
                if mat[i][j] == 'X':
                    row.append('X')
                else:
                    row.append('-')
            temp.append(row)

        for i in range(n):
            if temp[i][0] == '-':
                self.floodFillUtil(temp, i, 0, '-', 'O', n, m)
        for i in range(n):
            if temp[i][m - 1] == '-':
                self.floodFillUtil(temp, i, m - 1, '-', 'O', n, m)
        for i in range(m):
            if temp[0][i] == '-':
                self.floodFillUtil(temp, 0, i, '-', 'O', n, m)
        for i in range(m):
            if temp[n - 1][i] == '-':
                self.floodFillUtil(temp, n - 1, i, '-', 'O', n, m)

        for i in range(n):
            for j in range(m):
                if temp[i][j] == '-':
                    temp[i][j] = 'X'

        return temp