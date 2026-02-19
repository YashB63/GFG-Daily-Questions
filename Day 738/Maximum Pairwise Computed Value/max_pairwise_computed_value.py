class Solution:
    def findMax(self,arr):
        return max([i.feet*12+i.inches for i in arr])