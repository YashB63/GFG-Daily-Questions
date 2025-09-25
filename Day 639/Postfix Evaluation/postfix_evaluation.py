class Solution:
    def evaluatePostfix(self, arr):
        st = []
        for token in arr:
            if token[0].isdigit() or (len(token) > 1 and token[0] == '-'):
                st.append(int(token))
            else:
                val1 = st.pop()
                val2 = st.pop()

                if token == '+':
                    st.append(val2 + val1)
                elif token == '-':
                    st.append(val2 - val1)
                elif token == '*':
                    st.append(val2 * val1)
                elif token == '/':
                    st.append(val2 // val1)
                elif token == '^':
                    st.append(int(math.pow(val2, val1)))
        return st.pop()