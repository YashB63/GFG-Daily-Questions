class Solution:
    def pattern(self, N):
        
        if N==0:
            return [0]
        if N<0:
            return [N]
        if N%5==0:
            ha=[i for i in range(N, 4, -5)]
            return ha + [0] + ha[::-1]
        else:
            a=[i for i in range(N, -1, -5)]
        return a + [N%5-5] + a[::-1]