class Solution:
    def getLongestPrefix(self, s):
        n = len(s)
        if n <= 1:
            return -1

        pi = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = pi[j - 1]
            if s[i] == s[j]:
                j += 1
                pi[i] = j

        if pi[-1] == 0:
            return -1

        k = pi[-1]
        while k > 0:
            nxt = pi[k - 1]
            if nxt == 0:
                break
            k = nxt

        return n - k