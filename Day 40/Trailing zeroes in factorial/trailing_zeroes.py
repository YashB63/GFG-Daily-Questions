class Solution:
    def trailingZeroes(self, N):
    	 
        count = 0
        i = 5
        
        while N//i > 0:
            count += N//i
            i *= 5
        return count