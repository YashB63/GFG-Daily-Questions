class Solution:
    def uncommonChars(self, s1, s2):
        res = ''

        present = [0] * 26

        for e in s1:
            present[ord(e) - ord('a')] = 1

        for e in s2:
            if present[ord(e) - ord('a')] == 1 or present[ord(e) -
                                                          ord('a')] == -1:
                present[ord(e) - ord('a')] = -1
            else:
                present[ord(e) - ord('a')] = 2

        res = ''

        for i, e in enumerate(present):
            if e == 1 or e == 2:
                res += chr(i + ord('a'))
        return res