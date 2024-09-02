import math
class Solution:
    def minimumDays(self, S, N, M):
        if M>N:
            return -1
        if (N*6 <M*7 and S>6):
            return -1
        return math.ceil(M*S/N)