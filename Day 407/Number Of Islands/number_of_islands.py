from typing import List

class DS:
    def __init__(self, n):
        self.c = [i for i in range(n)]
        self.s = [1 for i in range(n)]
        
    def set_of(self, i):
        if i == self.c[i]:
            return i
        self.c[i] = self.set_of(self.c[i])
        return self.c[i]
        
    def merge(self, x, y):
        x, y = self.set_of(x), self.set_of(y)
        if x == y:
            return 0
        if self.s[x] < self.s[y]:
            x, y = y, x
        self.c[y] = x
        self.s[x] += self.s[y]
        return 1

class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        grid = [[0 for j in range(m)] for i in range(n)]
        
        def idx(i, j):
            return i *  m + j
        
        dsu = DS(n * m)
        di = [0, 0, -1, 1]
        dj = [1, -1, 0, 0]
        isl = []
        count = 0
        for item in operators:
            i, j = item
            if not grid[i][j]:
                count += 1
                grid[i][j] = 1
                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]
                    if ni >= 0 and ni < n and nj >= 0 and nj < m and grid[ni][nj]:
                        count -= dsu.merge(idx(i, j), idx(ni, nj))
            isl.append(count)
        return isl