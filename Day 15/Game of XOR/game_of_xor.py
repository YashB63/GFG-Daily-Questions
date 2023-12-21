class Solution:
    def gameOfXor(self, N , A):
        
        res = 0
        for i in range(N):
            count = (i+1) * (N-i)
            if count % 2 == 1:
                res ^= A[i]
        return res