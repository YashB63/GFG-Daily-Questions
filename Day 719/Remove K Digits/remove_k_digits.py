class Solution:
    def removeKdig(self, s, k):
        if len(s)==k:
            return 0
        
        stack = []
        
        for i in s:
            while stack and stack[-1]>i and k:
                stack.pop()
                k-=1
            stack.append(i)
        
        
        while(k and stack):
            stack.pop()
            k-=1
        
        for i in range(len(stack)):
            if stack[i]!="0":
                break
        
        return "".join(stack[i:])