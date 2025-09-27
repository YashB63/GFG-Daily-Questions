class Solution:
    def middle(self, a, b, c):
        if a < b:
            return b if b < c else max(a, c)
        else:
            if a < c:
                return a
            else:
                return max(b, c)