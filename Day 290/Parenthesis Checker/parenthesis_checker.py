class Solution:
    
    def ispar(self,x):
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
    
        for char in x:
            if char in bracket_map.values():
                stack.append(char)
            
            elif char in bracket_map:
               
                if stack == [] or stack[-1] != bracket_map[char]:
                    return False
               
                stack.pop()
        
        return stack == []