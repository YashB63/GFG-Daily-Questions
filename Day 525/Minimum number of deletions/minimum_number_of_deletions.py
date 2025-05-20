class Solution:

    def minDeletions(self, s):
        n = len(s)

        prev1 = [0] * n
        curr = [0] * n
        prev2 = [0] * n

        for l in range(2, n + 1):
            for i in range(n - l, -1, -1):
                j = i + l - 1

                if l == 2:
                    curr[i] = 0 if s[i] == s[j] else 1
                else:

                    if s[i] == s[j]:
                        curr[i] = prev2[i + 1]
                    else:
                        curr[i] = 1 + min(prev1[i], prev1[i + 1])

            prev2 = prev1[:]
            prev1 = curr[:]

        return prev1[0]