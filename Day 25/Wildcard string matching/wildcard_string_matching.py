import re

class Solution:
    def match(self, wild, pattern):
        
        reg_pattern = re.escape(wild).replace(r"\*", ".*").replace(r"\?", ".")
        
        res = re.fullmatch(reg_pattern, pattern)
        
        return res is not None
