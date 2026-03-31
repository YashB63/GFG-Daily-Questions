class Solution:
    def segregateEvenOdd(self, arr):
        x = []
        y = []
        for i in arr:
            if i % 2 == 0:
                x.append(i)
            else:
                y.append(i)
        x.sort()
        y.sort()
        arr[:] = x + y