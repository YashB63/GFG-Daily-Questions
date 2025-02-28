class Solution:
    def isBalanced(self, s):
        open_b=["(","{","["]
        close_b=[")","}","]"]
        stack=[]
        for i in s:
            if i in open_b:
                stack.append(i)
            else:
                if stack==[]:
                    return False
                else:
                    if stack[-1]==open_b[close_b.index(i)]:
                        stack.pop()
                    else:
                        return False
        if stack==[]:
            return True
        else:
            return False