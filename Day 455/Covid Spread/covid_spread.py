from collections import deque

class Solution:
    def helpaterp(self, hospital):
        r = len(hospital)
        c = len(hospital[0])
        
        q = deque()
        
        for i in range(r):
            for j in range(c):
                if hospital[i][j] == 2:
                    q.append((i, j))
        
        row = [-1, 1, 0, 0]
        col = [0, 0, -1, 1]
        
        def valid(i, j):
            return 0 <= i < r and 0 <= j < c
        
        timer = 0
        
        while q:
            timer += 1
            patient = len(q)
            
            for _ in range(patient):
                i, j = q.popleft()
                
                for k in range(4):
                    ni, nj = i + row[k], j + col[k]
                    if valid(ni, nj) and hospital[ni][nj] == 1:
                        hospital[ni][nj] = 2
                        q.append((ni, nj))
        
        for i in range(r):
            for j in range(c):
                if hospital[i][j] == 1:
                    return -1
        
        return timer - 1 if timer >0 else 0