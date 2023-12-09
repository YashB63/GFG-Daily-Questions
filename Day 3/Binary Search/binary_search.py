class Solution:	
	def binarysearch(self, arr, n, k):
        left, right = 0, n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == k:
                return mid
            elif arr[mid] < k:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
