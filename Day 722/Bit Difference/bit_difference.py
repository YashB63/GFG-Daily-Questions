class Solution:
    def countBits(self, N, A):
        out = 0
        for i in range(32):
            count = 0
            for j in range(N):
                if A[j] & (1<<i): count += 1
            out += (count*(N-count)*2)
        return out % (1000000007)