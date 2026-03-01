class Solution:
    def countZeroes(self, A, N):
        result = 0
        
        for i in A:
            result += (i.count(0))
        
        return result