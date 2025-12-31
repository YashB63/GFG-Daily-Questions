class Solution:
    def rowWithMax1s(self, arr):
        cMax = 0
        iMax = -1
        for i, row in enumerate(arr):
            if (row.count(1)>cMax):
                cMax = row.count(1)
                iMax = i  
        return iMax