class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        st = []
        res = ""

        for i in range(n):
            if s[i] == ' ':
                found = False
                while st:
                    res += st.pop()
                    found = True
                if found:
                    res += " "
            else:
                st.append(s[i])

        while st:
            res += st.pop()

        if res.endswith(" "):
            res = res[:-1]

        return res