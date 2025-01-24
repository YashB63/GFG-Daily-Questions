class Solution:
    def solve (self, X, Y, S):
        a = 'pr'
        b = 'rp'
        if X < Y:
            a, b = b, a
            X, Y = Y, X
            
        stack = []
        ans = 0
        for i in range(len(S)):
            if stack and S[i]==a[1] and stack[-1]==a[0]:
                stack.pop()
                ans += X
            else:
                stack.append(S[i])
                
        stack2 = []
        
        for i in range(len(stack)):
            if stack2 and stack[i] == b[1] and stack2[-1]==b[0]:
                stack2.pop()
                ans += Y
            else:
                stack2.append(stack[i])
        
        return ans