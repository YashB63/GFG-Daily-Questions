class Solution:
    def postToPre(self, post_exp):
        stack = []
        for char in post_exp:
            if char.isalnum():  
                stack.append(char)
            else:  
                op2 = stack.pop()
                op1 = stack.pop()
                new_expr = char + op1 + op2
                stack.append(new_expr)
        return stack[-1]