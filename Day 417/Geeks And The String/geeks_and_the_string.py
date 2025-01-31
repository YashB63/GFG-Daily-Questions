class Solution:
    def removePair(self,s):
        stack = []
        ans = ''
        for i in range(len(s)):
            if stack == []:
                stack.append(s[i])
            elif stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        if stack:
            for i in range(len(stack)):
                ans += stack[i]
        if len(ans)!=0:
            return ans
        else:
            return -1