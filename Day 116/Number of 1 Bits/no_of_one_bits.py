class Solution:
	def setBits(self, N):
		
        count = 0
        while N > 0:
            count += 1
            N = N & (N-1)
        return count