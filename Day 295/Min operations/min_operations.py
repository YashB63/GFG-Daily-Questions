class Solution:
    def solve(self, a : int, b : int) -> int:
        if a==b:
            return 0
        elif a==0 or b==0:
            return 1
        x=a&b
        if a==x or b==x:
            return 1
        else:
            return 2