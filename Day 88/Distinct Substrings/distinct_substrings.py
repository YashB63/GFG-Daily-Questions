class Solution:

    def fun(self, s):
        
        st = set()
        for i in range(1, len(s)):
            st.add(s[i - 1 : i + 1])
        return len(st)