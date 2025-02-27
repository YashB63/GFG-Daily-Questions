class Solution:
    def preToPost(self, pre_exp):
        st = []
        
        for i in range(len(pre_exp)-1,-1,-1):
            char = pre_exp[i]
            if char in '+-*^/%':
                operand1 = st.pop()
                operand2 = st.pop()
                new_operand = operand1 + operand2 + char
                st.append(new_operand)
            else:
                st.append(char)
        
        return st[-1]