class Solution:
    def findSmallest(self, arr):
        t = 1
        for i in arr:
            if t < i:
                return t
            t += i
        return t