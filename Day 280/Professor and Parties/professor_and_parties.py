class Solution:
    def PartyType(self, arr):
        seen = set()
        
        for color in arr:
            if color in seen:
                return "true"  
            seen.add(color)
        
        return "false"