class Solution:
    def buildLowestNumber(self, S,N):
        stack = []
        for digit in S:
            while N > 0 and stack and stack[-1] > digit:
                stack.pop()
                N -= 1
            stack.append(digit)
        
        while N > 0:
            stack.pop()
            N -= 1
        
        result = ''.join(stack).lstrip('0')
        return result if result else "0"