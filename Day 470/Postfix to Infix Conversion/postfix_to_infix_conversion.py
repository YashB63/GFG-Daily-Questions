class Solution:
    def postToInfix(self, postfix):
        stack=[]
        for char in postfix:
            if char.isalnum():
                stack.append(char)
            else:
                right=stack.pop()
                left=stack.pop()
                stack.append(f"({left}{char}{right})")
        return stack[-1]