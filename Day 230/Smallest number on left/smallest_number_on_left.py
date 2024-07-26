class Solution:
    def leftSmaller(self, n, a):
        
        stack=[-1]
        s=[0]*n
        for i in range(n):
            j=a[i]
            while stack[-1]>=j:
                stack.pop()
            s[i]=stack[-1]
            stack.append(j)
        return s