class Solution:
    def fibonacciNumbers(self, n):
        res = []

        a = 0
        b = 1

        if n > 0:
            res.append(0)
        if n > 1:
            res.append(1)

        for i in range(2, n):
            res.append(a + b)
            c = a + b
            a = b
            b = c

        return res