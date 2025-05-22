class Solution:
    def countSubstring(self, s):
        n = len(s)

        freq = [0] * 26

        for i in range(n):
            freq[ord(s[i]) - ord('a')] += 1

        count = 0

        for i in range(26):
            count += (freq[i] * (freq[i] + 1)) // 2

        return count