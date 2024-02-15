class Solution:
	def bracketNumbers(self, S):
		
        res = []
        count = 0
        stack = []
        for i in S:
            if i == '(':
                count += 1
                res.append(count)
                stack.append(count)
            if i == ')':
                res.append(stack.pop())
                
        return res