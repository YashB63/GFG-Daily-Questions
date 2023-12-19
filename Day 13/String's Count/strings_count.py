class Solution:

    def countStr(self, n):
        
        return (1 + (n*2) + (n*((n*n) -1) // 2))