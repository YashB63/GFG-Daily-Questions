def getZarr(string, z):
    n = len(string)

    l, r, k = 0, 0, 0
    for i in range(1, n):
        if i > r:
            l, r = i, i

            while r < n and string[r - l] == string[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:

            k = i - l

            if z[k] < r - i + 1:
                z[i] = z[k]

            else:
                l = i
                while r < n and string[r - l] == string[r]:
                    r += 1
                z[i] = r - l
                r -= 1
class Solution:
    def search(self, pattern, text):
        concat = pattern + "$" + text
        l = len(concat)
        res = []
        z = [0] * l
        getZarr(concat, z)

        for i in range(l):
            if z[i] == len(pattern):
                res.append(i-len(pattern))

        return res