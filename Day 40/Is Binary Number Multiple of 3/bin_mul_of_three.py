class Solution:
	def isDivisible(self, s):
		
        x = int(s, 2)
        if x%3 == 0:
            return 1
        else:
            return 0