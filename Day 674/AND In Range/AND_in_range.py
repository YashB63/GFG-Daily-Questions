class Solution:
    def andInRange(self, l, r):
        shiftCount = 0
        while l != r and l > 0:
            shiftCount += 1
            l = l >> 1
            r = r >> 1
        return (l << shiftCount)