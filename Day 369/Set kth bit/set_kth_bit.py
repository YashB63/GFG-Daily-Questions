class Solution:
	def setKthBit(self, N, K):
        k = 1<<K
        return N|k