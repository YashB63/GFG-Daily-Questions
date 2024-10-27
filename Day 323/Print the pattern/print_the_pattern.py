class Solution:
    def pattern(self, n):
        res = [''] * n
        counter = 1
        
        for i in range(n):
            s = ''
            for j in range(n - i):
                s += str(counter) + '*'
                counter += 1
            res[i] = s
        for i in range(n-1, -1, -1):
            s = ''
            for j in range(n - i):
                s += str(counter) + '*'
                counter += 1
            res[i] += s[:-1]
        for i in range(n):
            res[i] = ('-' * (i << 1)) + res[i]
        return res