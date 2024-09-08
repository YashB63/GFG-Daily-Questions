class Solution:
    def maxOnes (self, Mat, N, M):
        max = -1
        ind = -1
        for i in range(N):
            freq = Mat[i].count(1)
            if(freq>max):
                max = freq
                ind = i
        return ind