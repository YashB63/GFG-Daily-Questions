class Solution:
	def bracketNumbers(self, str):
		
        count = 0
        stack = []; b_count = []
        for char in str:
            if char == '(':
                count +=1
                stack.append(count)
                b_count.append(count)
            elif char ==')':
                b_count.append(stack.pop())
            
        return b_count