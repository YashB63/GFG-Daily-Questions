class Solution:
	def find(self, n):
        for i in range(n+1):
            if i*(i+1)==(2*n):
                return i
            elif i*(i+1)>(2*n):
                return -1