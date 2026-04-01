class Solution:
    def minWindow(self, s, p):
        if len(p) > len(s):
            return ""

        freq = [0]*26

        for c in p:
            freq[ord(c)-97] += 1

        left = 0
        count = len(p)
        min_len = float('inf')
        start = 0

        for right in range(len(s)):

            if freq[ord(s[right])-97] > 0:
                count -= 1

            freq[ord(s[right])-97] -= 1

            while count == 0:

                if right-left+1 < min_len:
                    min_len = right-left+1
                    start = left

                freq[ord(s[left])-97] += 1

                if freq[ord(s[left])-97] > 0:
                    count += 1

                left += 1

        if min_len == float('inf'):
            return ""

        return s[start:start+min_len]