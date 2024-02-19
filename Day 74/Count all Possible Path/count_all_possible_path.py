class Solution:
	def isPossible(self, paths):
		
        return int(all(sum(i)%2 == 0 for i in paths))