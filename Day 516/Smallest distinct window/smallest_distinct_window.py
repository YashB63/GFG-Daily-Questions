class Solution:
    def findSubString(self, s):
        d = len(set(s))
        i = j = c = 0
        res = len(s)
        freq = [0]*256
        while j < len(s):
            if freq[ord(s[j])] == 0:
                c += 1
            freq[ord(s[j])] += 1
            j += 1
            while c == d:
                res = min(res, j - i)
                freq[ord(s[i])] -= 1
                if freq[ord(s[i])] == 0:
                    c -= 1
                i += 1
        return res