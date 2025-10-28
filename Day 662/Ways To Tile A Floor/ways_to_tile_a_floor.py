class Solution:
    def numberOfWays(self, n: int) -> int:
        if n <= 3:
            return n  
        pre2 = 1
        pre1 = 2
        for i in range(3, n + 1):
            t = pre1 + pre2
            pre2 = pre1
            pre1 = t
        return pre1