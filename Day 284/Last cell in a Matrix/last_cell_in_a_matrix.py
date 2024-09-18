class Solution:
    def endPoints(self, matrix, R, C):
        r = 0
        c=0
        d = 0
        dir_dc = {0: (0, 1), 1: (1,0), 2: (0, -1), 3 : (-1, 0)}
        while 0 <=r < R and 0 <= c < C:
            ans = (r,c)
            if matrix[r][c] == 1:
                d = (d + 1) % 4
                matrix[r][c] = 0
            c = c + dir_dc[d][1]
            
            r = r + dir_dc[d][0]
        return ans