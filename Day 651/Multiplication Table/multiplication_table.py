class Solution:
    def getTable(self, n):
        arr = []
        for i in range(1, 11):
            arr.append(n * i)
        return arr