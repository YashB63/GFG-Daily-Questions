class Solution:
	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
        max_till_here = arr[0]
        min_till_here = arr[0]
        total_max = arr[0]
        
        for i in range(1, n):
            temp_max = max(arr[i], max_till_here * arr[i], min_till_here * arr[i])
            min_till_here = min(arr[i], max_till_here * arr[i], min_till_here * arr[i])
            max_till_here = temp_max
            total_max = max(total_max, max_till_here)
        
        return total_max