class Solution:
    def longest(self, names):
        n = len(names)
        m = 0

        for i in range(1, n):
            if len(names[i]) > len(names[m]):
                m = i

        return names[m]