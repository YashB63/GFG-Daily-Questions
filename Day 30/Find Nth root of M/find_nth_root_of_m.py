class Solution:
	def NthRoot(self, n, m):
		
        left = 1
        right = m
        
        while(left <= right):
            middle = left + (right - left) // 2
            
            if middle**n == m:
                return middle
            
            elif middle**n > m:
                right = middle - 1
                
            else:
                left = middle + 1
                
        return -1