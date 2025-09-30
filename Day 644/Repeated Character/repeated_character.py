class Solution:
    def firstRep(self, s):
        dicti = {}

        for i in s:
            if i in dicti:
                dicti[i] += 1
            else:
                dicti[i] = 1

        for i in s:
            if dicti[i] > 1:
                return i

        return -1