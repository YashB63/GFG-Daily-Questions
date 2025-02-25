class Solution:
    def SaveGotham(self,arr) : 
        MODULO = 10**9 + 7
        s = []
        total_height = 0
        for a in reversed(arr):
            while s and s[-1] <= a:
                s.pop()
            if s:
                total_height = (total_height + s[-1]) % MODULO
            s.append(a)
        return total_height