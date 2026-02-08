class Solution:
    def palindromicSubstr(self, s):
        n = len(s)

        result = set()

        for i in range(n):
            left = i
            right = i
            while left >= 0 and right < n and s[left] == s[right]:

                result.add(s[left:right + 1])
                left -= 1
                right += 1

        for i in range(n - 1):
            left = i
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:

                result.add(s[left:right + 1])
                left -= 1
                right += 1

        res = list(result)
        return res