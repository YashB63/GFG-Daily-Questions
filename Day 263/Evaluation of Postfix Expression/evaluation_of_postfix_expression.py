class Solution:
    def evaluatePostfix(self, S):
        st = []
        for i in S:
            if i.isnumeric():
                st.append(int(i))
            else:
                s = st.pop()
                f = st.pop()
                if i == '+':
                    st.append(f + s)
                elif i == '-':
                    st.append(f - s)
                elif i == '/':
                    st.append(f // s)
                elif i == '*':
                    st.append(f * s)
        return st.pop()