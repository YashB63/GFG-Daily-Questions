class Solution:
    def AllParenthesis(self,n):
        stack=[]
        res=[]
        def backtrack(openn,closen):
            if openn==closen==n:
                res.append("".join(stack))
            if openn<n:
                stack.append("(")
                backtrack(openn+1,closen)
                stack.pop()
                
            if closen<openn:
                stack.append(")")
                backtrack(openn,closen+1)
                stack.pop()
                
        backtrack(0,0)
        return res