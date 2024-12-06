from math import ceil

class Solution:
    def noOfDays(self, R, S, Q):
        return ceil(1.0 * (Q-S) / (R-S))