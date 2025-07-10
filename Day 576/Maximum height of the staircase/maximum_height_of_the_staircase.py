import math

class Solution:
    def maxStairHeight(self, N):
        ans = int(math.sqrt(2.0 * N + 0.25) - 0.5)
        return ans