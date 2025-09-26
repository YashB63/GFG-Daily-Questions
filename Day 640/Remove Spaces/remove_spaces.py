class Solution:
    def modify(self, s):
        n = len(s)
        i, itr = 0, 0
        chars = list(s)

        while i < n:
            if chars[i] != ' ':
                chars[itr] = chars[i]
                itr += 1
            i += 1

        return ''.join(chars[:itr])