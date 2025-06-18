class Solution:
    def MaxGold(self, mat):
        f = False
        for i in range(len(mat[0])):
            if mat[0][i] > -1:
                f = True
                break
        
        if f == False:
            return 0
        r, c, maxx = len(mat), len(mat[0]), 0
        
        for i in range(r):
            for j in range(c):
                if i == 0:
                    maxx = max(mat[i][j], maxx)
                    continue
                if mat[i][j] == -1:
                    continue
                
                x = mat[i - 1][j]
                y = mat[i - 1][j - 1] if j - 1 >= 0 else -1
                z = mat[i - 1][j + 1] if (j + 1) < c else -1
                
                if x == y == z == -1:
                    mat[i][j] = -1
                    continue
                
                mat[i][j] += max(x, y, z)
                
                maxx = max(maxx, mat[i][j])
        
        return maxx