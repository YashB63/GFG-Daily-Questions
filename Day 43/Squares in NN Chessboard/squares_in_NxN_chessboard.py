class Solution:
    def squaresInChessBoard(self, N):
        
        res = (N * (N + 1) * (2 * N + 1)) // 6
        return res