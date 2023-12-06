class Solution:

	def findMaximum(self,arr, n):
        left = 0
        right = n - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
                
        return arr[left]