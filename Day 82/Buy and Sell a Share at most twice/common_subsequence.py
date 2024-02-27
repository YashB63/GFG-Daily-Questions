class Solution:
	def commonSubseq(self, a, b):
		
        a = set(a) & set(b)
        return ''.join(a)