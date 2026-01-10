class Solution:
    def wordBreak(self, dict, s):
        st = set(dict)
        n = len(s)

        dp = [[] for _ in range(n + 1)]

        dp[n].append("")

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                word = s[i:j]

                if word in st:
                    for sub in dp[j]:
                        if sub:
                            dp[i].append(word + " " + sub)
                        else:
                            dp[i].append(word)

        return dp[0]