class Solution:
    def solve(self, n: int, a: list, b: int) -> int:
        for ele in a:
            if(ele == b):
                b = b * 2
        
        return b