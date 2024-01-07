class Solution:

	def print2largest(self,arr, n):
		
		arr.sort(reverse=True)
		
		largest = arr[0]
		
		for num in arr:
		    if num < largest:
		        return num
		        
        return -1