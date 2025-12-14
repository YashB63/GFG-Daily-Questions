class Solution:
    def concatenatedString(self, s1, s2):
        res = ""
        m = {}

        for i in range(0, len(s2)):
            m[s2[i]] = 1

        for i in range(0, len(s1)):
            if (not s1[i] in m):
                res = res + s1[i]
            else:
                m[s1[i]] = 2

        for i in range(0, len(s2)):
            if (m[s2[i]] == 1):
                res = res + s2[i]

        if (res == ""):
            res = "-1"

        return res