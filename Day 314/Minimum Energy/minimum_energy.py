class Solution:
    def minEnergy(self, arr):
        e = 0
        res = 0
        for num in arr:
            e+=num
            if e <=0:
                res += abs(e) +1
                e = 1
        return res if res else 1