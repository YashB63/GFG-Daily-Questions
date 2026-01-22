class Solution:
	def reverseSubArray(self,arr,l,r):
	    left = l-1 
	    right = r-1 
		while left < right:
		    arr[left],arr[right] = arr[right],arr[left]
		    left += 1
		    right -= 1
		return arr