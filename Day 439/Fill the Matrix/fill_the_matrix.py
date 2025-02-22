from collections import deque

class Solution:
    def minIteration(self, N, M, x, y):
        return max(x-1, N-x) + max(y-1, M-y)