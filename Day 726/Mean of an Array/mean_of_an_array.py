from math import floor

class Solution:
    def findMean(self, arr):
        return floor(sum(arr)/len(arr))