class Solution:
	
	def findMaxSum(self,arr, n):
		
        if n == 1:
            return arr[0]
            
        x = arr[0]
        y = 0
        
        for i in range(1, n):
            new_y = max(x, y)
            x = y + arr[i]
            y = new_y
            
        return max(x, y)