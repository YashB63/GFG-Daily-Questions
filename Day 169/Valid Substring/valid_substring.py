class Solution:
    def findMaxLen(ob, S):
        
        maxx=0
        stack=[-1]
        for i in range(len(S)):
            if S[i]=="(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                maxx=max(maxx,i-stack[-1])
        return maxx