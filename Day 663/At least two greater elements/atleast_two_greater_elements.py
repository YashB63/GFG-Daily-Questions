class Solution:
    def findElements(self, arr):
        arr.sort()
        return arr[:len(arr) - 2]