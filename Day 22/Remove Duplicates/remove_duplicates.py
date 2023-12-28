class Solution:
	def removeDups(self, S):
		
        x = ""
        for i in S:
            if i not in x:
                x += i
        return x