class Solution:
    def isPossiblePalindrome(self, s, K):
        n = len(s)
        prev = [0] * n

        for i in range(n - 2, -1, -1):
            curr = prev[:]
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = 1 + min(prev[j], curr[j - 1])
            prev = curr

        min_changes_needed = prev[n - 1]
        return 1 if min_changes_needed <= K else 0