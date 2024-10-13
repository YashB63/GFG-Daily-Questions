class Solution:
	def KthLSB(self, n, k):
        return (n >>(k-1) & 1)