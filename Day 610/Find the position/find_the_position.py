class Solution:
    def findpos(self, n: str) -> int:
        pos = 0

        for ch in n:
            if ch == '4':
                pos = pos * 2 + 1  
            elif ch == '7':
                pos = pos * 2 + 2  
                
        return pos