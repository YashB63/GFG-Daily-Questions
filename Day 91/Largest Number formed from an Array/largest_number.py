from functools import cmp_to_key

class Solution:

	def printLargest(self, n, arr):
	    
        return str(int("".join(sorted(arr, key= cmp_to_key(lambda a,b : -1 if (a+b) > (b+a) else 1 )))))
