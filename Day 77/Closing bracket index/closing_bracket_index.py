class Solution:
    def closing (self,s, pos):
        
        op_count = 1
        c1_count = 0
        for i in range(pos+1, len(s)):
            if s[i] == ']':
                c1_count += 1
            elif s[i] == "[":
                op_count += 1
                
            if op_count == c1_count:
                return i