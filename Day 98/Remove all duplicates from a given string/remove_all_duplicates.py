class Solution:

	def removeDuplicates(self,str):
	    
        vis = ''
        for i in str:
            if i not in vis:
                vis+=i
        return vis