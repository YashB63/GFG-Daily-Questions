class Solution:
    def RedOrGreen(self, N, S):
        green = S.count("G")
        red = S.count("R")
        return min(red, green)