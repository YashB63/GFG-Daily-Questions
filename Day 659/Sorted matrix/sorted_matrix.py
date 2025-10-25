class Solution:
    def sortedMatrix(self, N, Mat):
        v = []
        for i in range(N):
            for j in range(N):
                v.append(Mat[i][j])
        
        v.sort()
        
        c = 0
        for i in range(N):
            for j in range(N):
                Mat[i][j] = v[c]
                c += 1
        
        return Mat