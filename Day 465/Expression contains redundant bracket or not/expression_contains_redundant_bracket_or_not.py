class Solution():

    def checkRedundancy(self, arr):
        stack = []
        for ele in arr:
            if ele == ')':
                top = stack[-1]
                stack.pop()
                
                flag = 1
                
                while top != '(':
                    if top in {'+', '-', '*', '/'}:
                        flag = 0
                    
                    top = stack[-1]
                    stack.pop()
                
                if flag:
                    return 1
            else:
                stack.append(ele)
        return 0