class Solution: 
    def asciirange(self, s):
        n = len(s)
        pref = [0] * (n + 1)
        v = [[] for _ in range(26)]

        for i in range(1, n + 1):
            idx = ord(s[i - 1]) - ord('a')
            if not v[idx]:
                v[idx].append(i)
                v[idx].append(i)
            else:
                v[idx][1] = i
            pref[i] = pref[i - 1] + ord(s[i - 1])

        ans = []
        for i in range(26):
            if v[i]:
                fi, se = v[i][0], v[i][1]
                if fi != se:
                    sum_val = pref[se - 1] - pref[fi]
                    if sum_val != 0:
                        ans.append(sum_val)

        return ans