class Solution:
    def match(self, curr, res):
        if curr > res:
            res = curr
        return res

    def swap(self, s, i, j):
        s_list = list(s)
        s_list[i], s_list[j] = s_list[j], s_list[i]
        return ''.join(s_list)

    def setDigit(self, s, index, res, k):
        if k == 0 or index == len(s) - 1:
            return self.match(s, res)

        maxDigit = max(int(s[i]) for i in range(index, len(s)))

        if int(s[index]) == maxDigit:
            return self.setDigit(s, index + 1, res, k)

        for i in range(len(s) - 1, index, -1):
            if int(s[i]) == maxDigit:
                swapped = self.swap(s, index, i)
                res = self.setDigit(swapped, index + 1, res, k - 1)
        return res

    def findMaximumNum(self, s, k):
        return self.setDigit(s, 0, s, k)