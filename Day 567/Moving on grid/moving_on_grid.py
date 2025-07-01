class Solution:
    def movOnGrid(self, r, c):
        if (r - 1) % 7 == (c - 1) % 4:
            return 'ARYA'
        else:
            return 'JON'