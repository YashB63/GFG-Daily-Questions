class Solution:
    def reverse(self, s: str) -> str: 
        stack = []
        
        for ch in s:
            stack.append(ch)
            
        rev_str = ""
        while stack:
            rev_str += stack.pop()
        
        return rev_str