class Solution():
    def solve(self, N, A):
        
        for i in range(N-1, -1, -1):
            if A[i] < 9:
                return i + 1