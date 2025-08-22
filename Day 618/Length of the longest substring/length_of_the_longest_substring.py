class Solution:
    def longestUniqueSubstring(self, s):
        n = len(s)

        cur_len = 0  

        max_len = 0  

        visited = {}

        for i in range(n):
            if s[i] in visited and i - cur_len <= visited[s[i]]:
                cur_len = i - visited[s[i]]
            else:
                cur_len += 1

            visited[s[i]] = i

            if cur_len > max_len:
                max_len = cur_len

        return max_len